from .models import Mcq,  Test, Course
from .serializers import McqSerializer, TestSerializer, CourseSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError

class McqList(APIView):
    # ! Get all questions
    def get(self, request, format=None):
        mcqs = Mcq.objects.all()
        serializer = McqSerializer(mcqs, many=True)
        return Response(serializer.data)


class McqDetails(APIView):

    def get_object(self, pk):
        try:
            return Mcq.objects.get(id=pk)  # type: ignore
        except Mcq.DoesNotExist:   
            raise Http404

    #  ! Get a particular question
    def get(self, request, pk):
        mcq = self.get_object(pk) # type: ignore
        serializer = McqSerializer(mcq)
        return Response(serializer.data)
    
    #  ! Update a question
    def put(self, request, pk, format=None):
        mcq = self.get_object(pk)
        serializer = McqSerializer(mcq, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ! Delete a question
    def delete(self, request, pk, format=None):
        mcq = self.get_object(pk)
        mcq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # ! Add a question
    def post(self, request, format=None):
        serializer = McqSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError as e:
                e ={"error": 'this data already exists in the database'}
                return Response(e)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestList(APIView):
    # ! Get all tests
    def get (self, request):
        test = Test.objects.all()  # type: ignore
        serializer = TestSerializer(test, many=True)
        return Response(serializer.data)

class TestDetails(APIView):

    def get_object(self, pk):
        try:
            return Test.objects.get(id=pk)  # type: ignore
        except Test.DoesNotExist:  # type: ignore
            raise Http404

    #  ! Get a particular test
    def get(self, request, pk):
        test =  self.get_object(pk)
        serializer = TestSerializer(test)
        return Response(serializer.data)

    #  ! Update a test
    def put(self, request, pk, format=None):
        test = self.get_object(pk)
        serializer = TestSerializer(test, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # ! Delete a test
    def delete(self, request, pk, format=None):
        test = self.get_object(pk)
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # ! Add a test
    def post(self, request, format=None):
        serializer = TestSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseList(APIView):
    # ! Get all courses
    def get(self, request):
        course = Course.objects.all()  # type: ignore
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

class CourseDetails(APIView):

    def get_object(self, pk):
        try:
            return Course.objects.get(id=pk)  # type: ignore
        except Course.DoesNotExist:  # type: ignore
            raise Http404

    #  ! Get a particular course
    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    #  ! Update a course
    def put(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # ! Delete a course
    def delete(self, request, pk, format=None):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # ! Add a course
    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError as e:
                e ={"error": 'this data already exists in the database'}
                return Response(e)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


