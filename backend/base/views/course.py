from ..models import Course
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from ..serializers import CompanySerializer, CourseSerializer

class CourseViewSet(viewsets.ViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    query = Course.objects.all()
    serializer_class = CourseSerializer

    def list(self, request):
        serializer = self.serializer_class(self.query, many=True)
        return Response({'status': 200, 'data': serializer.data}, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        course = get_object_or_404(self.query, pk=pk)
        serializer = self.serializer_class(course)
        return Response({'status': 201, 'data': serializer.data}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        course = get_object_or_404(self.query, pk=pk)
        serializer = self.serializer_class(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def partial_update(self, request, pk=None):
        course = get_object_or_404(self.query, pk=pk)
        serializer = self.serializer_class(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        course = get_object_or_404(self.query, pk=pk)
        course.delete()
        return Response({'status': 204, 'data': None}, status=status.HTTP_204_NO_CONTENT)
