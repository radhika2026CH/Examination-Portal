from distutils.ccompiler import new_compiler
from django.shortcuts import render
from .models import Student
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken
from django.core import serializers

# ! Get User Information from JWT Token
def get_user_from_JWT(access_token_str):
    access_token_obj = AccessToken(access_token_str)
    user_id=access_token_obj['user_id']
    content =  {'user_id': user_id}
    return (content)

def is_member(user):
    if user.groups.filter(name='staff').exists():
        return "staff"
    return "student"

# ! User registration
class UserRegister(APIView):
    def post(self, request):
        try:
            username = request.POST.get("username")
            fname = request.POST.get("fname")
            lname = request.POST.get("lname")
            email = request.POST.get("email")
            password = request.POST.get("password")
            group = request.POST.get("group")
            print(group)
            new_user = User.objects.create_user(username, email, password)
            new_user.first_name = fname
            new_user.last_name = lname
            grouped = Group.objects.get(name=group)
            new_user.groups.add(grouped)
            new_user.save()
            refresh = RefreshToken.for_user(new_user)
            return Response({
                "success": "User Created Successfully",
                "refresh": str(refresh),
                "access": str(refresh.access_token)})
        except Exception as e:
            return Response({"error": e.args})

# ! Login 
class UserLogin(APIView):
    def post(self, request):
        username =  request.POST.get("username")
        password = request.POST.get("password")
        auth = authenticate(username=username, password=password)
        if auth:
            login(request, auth)
            user =User.objects.filter(username=username).first()
            print("USER\n\n\n", user.id)
            print("is_active", user.is_active)
            if user.is_active == False:
                return  Response({"error": "Your account has been deactivated"})
            refresh = RefreshToken.for_user(user)
            return Response({
                            "success": status.HTTP_200_OK,
                            "refresh": str(refresh),
                            "access": str(refresh.access_token)
                            })
        else:
            return Response({"error": status.HTTP_401_UNAUTHORIZED})

# ! Logout
def logoutUser(request):
    logout(request)
    return HttpResponse({"status": status.HTTP_200_OK})


# ! Logged In User CRUD
class UserDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_user_details(self, token):
        token = token[7: ] 
        content = get_user_from_JWT(token)
        id = content['user_id']
        try:
            return User.objects.filter(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        try:
            token = request.headers['Authorization']
            user = self.get_user_details(token).first()
            print("ok")
            group = is_member(user)
            print("Group", group)
            user = self.get_user_details(token).values()
            return Response({"success": status.HTTP_200_OK, "user_detail": list(user), "group": group })
        except Exception as e:
            return Response({'error': e.args})

    # ! Deactivate user based on hierarchy (Super User > Staff > Student)
    def delete(self, request):
        token = request.headers['Authorization']
        user = self.get_user_details(token).first()
        user_id_to_deactive = request.data['user_id_to_deactive']
        user_to_deactivate = User.objects.filter(username=user_id_to_deactive).first()

        if user_to_deactivate.is_active == False:
            return  Response({"error": "user is already deactivated"})   

        
        if is_member(user_to_deactivate) == "student": 
            if is_member(user) == "student":
                return  Response({"error": "you do not have the access", "status": status.HTTP_403_FORBIDDEN})
            else:
                user_to_deactivate.is_active = False
                user_to_deactivate.save()
                return Response({"success": "Successful"})
        else:
            if user.is_superuser:
                user_to_deactivate.is_active = False
                user_to_deactivate.save()
                return Response({"success": "Successful"})
            else: 
                return  Response({"error": "you do not have the access", "status": status.HTTP_403_FORBIDDEN})
        
    # # def update(self, request):



# ! Get all Students
class AllStudent(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try: 
            Students = User.objects.filter(groups__name="student").values()
            return Response({"success": status.HTTP_200_OK, "students_detail_list": list(Students) })
        except Exception as e:
                return Response({'error': e.args})

# ! Get all Staffs
class AllStaff(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try: 
            Students = User.objects.filter(groups__name="staff").values()
            return Response({"success": status.HTTP_200_OK, "staff_detail_list": list(Students) })
        except Exception as e:
                return Response({'error': e.args})       

