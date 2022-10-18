from .models import Staff
from .serializers import StaffSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError


class StaffList(APIView):
    def get(self, request, format=None):
        staff = Staff.objects.all()
        serializer = StaffSerializers(staff, many=True)
        return Response(serializer.data)
    

class StaffDetail(APIView):
    def get_object(self, pk):
        try:
            return Staff.objects.get(id=pk)
        except Staff.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        staff = self.get_object(pk)
        serializer = StaffSerializers(staff)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        staff = self.get_object(pk)
        serializer = StaffSerializers(staff, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        staff = self.get_object(pk)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        serializer = StaffSerializers(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError as e:
                e ={"error": 'this data already exists in the database'}
                return Response(e, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
