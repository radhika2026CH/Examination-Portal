# from .models import Mcq,  Test, Course
# from .serializers import McqSerializer, TestSerializer, CourseSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.db import IntegrityError

# class McqList(APIView):
#     # ! Get all questions
#     def get(self, request, format=None):
#         mcqs = Mcq.objects.all()
#         serializer = McqSerializer(mcqs, many=True)
#         return Response(serializer.data)


# class McqDetails(APIView):

#     def get_object(self, pk):
#         try:
#             return Mcq.objects.get(id=pk)  # type: ignore
#         except Mcq.DoesNotExist:   
#             raise Http404

#     #  ! Get a particular question
#     def get(self, request, pk):
#         mcq = self.get_object(pk) # type: ignore
#         serializer = McqSerializer(mcq)
#         return Response(serializer.data)
    
#     #  ! Update a question
#     def put(self, request, pk, format=None):
#         mcq = self.get_object(pk)
#         serializer = McqSerializer(mcq, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # ! Delete a question
#     def delete(self, request, pk, format=None):
#         mcq = self.get_object(pk)
#         mcq.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     # ! Add a question
#     def post(self, request, format=None):
#         serializer = McqSerializer(data=request.data, context={"request": request})
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#             except IntegrityError as e:
#                 e ={"error": 'this data already exists in the database'}
#                 return Response(e)
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TestList(APIView):
#     # ! Get all tests
#     def get (self, request):
#         test = Test.objects.all()  # type: ignore
#         serializer = TestSerializer(test, many=True)
#         return Response(serializer.data)

# class TestDetails(APIView):

#     def get_object(self, pk):
#         try:
#             return Test.objects.get(id=pk)  # type: ignore
#         except Test.DoesNotExist:  # type: ignore
#             raise Http404

#     #  ! Get a particular test
#     def get(self, request, pk):
#         test =  self.get_object(pk)
#         serializer = TestSerializer(test)
#         return Response(serializer.data)

#     #  ! Update a test
#     def put(self, request, pk, format=None):
#         test = self.get_object(pk)
#         serializer = TestSerializer(test, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     # ! Delete a test
#     def delete(self, request, pk, format=None):
#         test = self.get_object(pk)
#         test.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     # ! Add a test
#     def post(self, request, format=None):
#         serializer = TestSerializer(data=request.data, context={"request": request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CourseList(APIView):
#     # ! Get all courses
#     def get(self, request):
#         course = Course.objects.all()  # type: ignore
#         serializer = CourseSerializer(course, many=True)
#         return Response(serializer.data)

# class CourseDetails(APIView):

#     def get_object(self, pk):
#         try:
#             return Course.objects.get(id=pk)  # type: ignore
#         except Course.DoesNotExist:  # type: ignore
#             raise Http404

#     #  ! Get a particular course
#     def get(self, request, pk):
#         course = self.get_object(pk)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)

#     #  ! Update a course
#     def put(self, request, pk, format=None):
#         course = self.get_object(pk)
#         serializer = CourseSerializer(course, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     # ! Delete a course
#     def delete(self, request, pk, format=None):
#         course = self.get_object(pk)
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     # ! Add a course
#     def post(self, request, format=None):
#         serializer = CourseSerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#             except IntegrityError as e:
#                 e ={"error": 'this data already exists in the database'}
#                 return Response(e)
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from cgi import test
from django.shortcuts import render
from .models import Course, SelectedAnswers, StudentCourse, Test, Question, TestAppeared  
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer, SelectedAnswerSerializer, StudentCourseSerializer, TestAppearedSerializer, TestSerializer, QuestionSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken
from django.core import serializers
from django.db import IntegrityError

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

class AllCourses(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # ! Get all courses
    def get(self, request):
        try: 
            course = Course.objects.all()  
            serializer = CourseSerializer(course, many=True)
            return Response({"success": status.HTTP_200_OK, "course_detail_list": serializer.data})
        except Exception as e:
            return Response({"error": e.args})


class CourseDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Course.objects.get(id=pk)  
        except Course.DoesNotExist:  
            raise Http404

    #  ! Get a particular course
    def get(self, request, pk, format=None):
        try:
            course = self.get_object(pk)
            serializer = CourseSerializer(course)
            return Response({"success": status.HTTP_200_OK, "course detail": serializer.data})
        except Exception as e:
            return Response({"error": e.args})
    
    #  ! Update a course
    def put(self, request, pk, format=None):
        try:
            snippet = self.get_object(pk)
            serializer = CourseSerializer(snippet, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response({"success": status.HTTP_200_OK, "course detail": serializer.data})
        except Exception as e:
            return Response({"error": e.args})

    # ! Delete a course
    def delete(self, request, pk, format=None):
        try: 
            course = self.get_object(pk)
            course.delete()
            return Response({"success": status.HTTP_200_OK})
        except Exception as e:
            return Response({"error": e.args})
            
    # ! Create a course
    def post(self, request, format=None):
            serializer = CourseSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    serializer.save()
                except Exception as e:
                    return Response({"error": e.args})
                return Response({"success": status.HTTP_200_OK, "course detail": serializer.data})
            else:
                return Response({"error": "something went wrong"})

# ! Get all tests
class AllTests(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try: 
            test = Test.objects.all()  
            serializer = TestSerializer(test, many=True)
            return Response({"success": status.HTTP_200_OK, "test_detail_list": serializer.data})
        except Exception as e:
            return Response({"error": e.args})

# ! Get all tests By Course Id
class AllTestsByCourseId(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            test = Test.objects.all().filter(fk_course_id=pk)
            serializer = TestSerializer(test, many=True)
            return Response({"success": status.HTTP_200_OK, "test_detail_list": serializer.data})
        except Exception as e:
            return Response({"error": e.args})

class TestDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Test.objects.get(id=pk)  
        except Test.DoesNotExist:  
            raise Http404

    #  ! Get a particular test
    def get(self, request, pk, format=None):
        try:
            test = self.get_object(pk)
            serializer = TestSerializer(test)
            return Response({"success": status.HTTP_200_OK, "test detail": serializer.data})
        except Exception as e:
            return Response({"error": e.args})
    
    #  ! Update a test
    def put(self, request, pk, format=None):
        try:
            snippet = self.get_object(pk)
            serializer = TestSerializer(snippet, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response({"success": status.HTTP_200_OK, "test detail": serializer.data})
        except Exception as e:
            return Response({"error": e.args})

    # ! Delete a test
    def delete(self, request, pk, format=None):
        try: 
            test = self.get_object(pk)
            test.delete()
            return Response({"success": status.HTTP_200_OK})
        except Exception as e:
            return Response({"error": e.args})

    # ! Add a test
    def post(self, request, format=None):
        try:
            serializer = TestSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({"success": status.HTTP_200_OK, "test detail": serializer.data})
        except Exception as e:
            return Response({"error": e.args})

# ! Get all questions
class AllQuestion(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            questions = Question.objects.all()  
            serializer = QuestionSerializer(questions, many=True)
            return Response({"success": status.HTTP_200_OK, "questions_detail_list": serializer.data})
        except Exception as e:
            return Response({"error": e.args})
    
# ! Get all questions By Test Id
class AllQuestionsByTestId(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try: 
            question = Question.objects.all().filter(fk_test_id=pk)
            serializer = QuestionSerializer(question, many=True)
            print(serializer.data)
            return Response({"success": status.HTTP_200_OK, "questions_detail_list": serializer.data})
        except Exception as e:
            return Response({"error": e.args})


class QuestionDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # ! Get question by Id
    def get(self, request, pk):
        try:
            question = get_object(pk)
            serializer = QuestionSerializer(test)
            return Response({"success": status.HTTP_200_OK, "questions detail": serializer.data})
        except Exception as e:
            return Response({"error": e.args})

    def get_object(self, pk):
        try:
            return Question.objects.get(id=pk)  
        except Question.DoesNotExist:  
            raise Http404

    #  ! Update a question
    def put(self, request, pk, format=None):
        try: 
            snippet = self.get_object(pk)
            serializer = QuestionSerializer(snippet, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response({"success": status.HTTP_200_OK, "questions detail": serializer.data})
        except Exception as e:
            return Response({"error": e.args})

    # ! Delete a question
    def delete(self, request, pk, format=None):
        try: 
            test = self.get_object(pk)
            test.delete()
            return Response({"success": status.HTTP_200_OK})
        except Exception as e:
            return Response({"error": e.args})

    # ! Add a question
    def post(self, request, format=None):
        try: 
            serializer = QuestionSerializer(data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            return Response({"success": status.HTTP_200_OK, "questions detail": serializer.data})
        except Exception as e:
            return Response({"error": e.args})

class StudentCourseView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    # ! Get all the students registered in different courses
    def get(self, request):
        test = StudentCourse.objects.filter(student = request.user)
        serializer = StudentCourseSerializer(test, many = True)
        return Response(serializer.data)

    # ! Add a student to a course
    def post(self, request):
        try: 
            serializer = StudentCourseSerializer(data = request.data, context = {'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({"success": status.HTTP_200_OK, "student course detail": serializer.data})
        except Exception as e:
            return Response({"error": e.args})

    # ! Get a particular row from the table
    def get_object(self, pk):
        try:
            return StudentCourse.objects.get(id=pk)  
        except StudentCourse.DoesNotExist:  
            raise Http404
    # ! Remove student from a course 
    def delete(self, request, pk, format=None):
        test = self.get_object(pk)
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class TestAppearedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # ! Get score of all the tests appeared by the student
    def get(self, request):
        test = TestAppeared.objects.filter(student = request.user)
        serializer = TestAppearedSerializer(test, many = True)
        return Response(serializer.data)
    # ! Create a new entry for a test appeared by the student 
    def post(self, request):
        serializer = TestAppearedSerializer(data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SelectedAnswersView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # ! Get the selected answers for a particular test for a particular user 
    def get(self, request, pk, format=None):
        snippet = SelectedAnswers.objects.filter(test=pk, student=request.user)
        serializer = SelectedAnswerSerializer(snippet, many = True)
        return Response(serializer.data)
    # ! Add a new answer for a particular question 
    def post(self, request):
        serializer = SelectedAnswerSerializer(data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
