from ..models import WorkExperience
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from ..serializers import WorkExperienceSerializer

class WorkExperienceViewSet(viewsets.ViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    query = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

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
        workExperience = get_object_or_404(self.query, pk=pk)
        serializer = self.serializer_class(workExperience)
        return Response({'status': 200, 'data': serializer.data}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        workExperience = get_object_or_404(self.query, pk=pk)
        serializer = self.serializer_class(workExperience, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors)
        
    def partial_update(self, request, pk=None):
        workExperience = get_object_or_404(self.query, pk=pk)
        serializer = self.serializer_class(workExperience, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        workExperience = get_object_or_404(self.query, pk=pk)
        workExperience.delete()
        return Response({'status': 204, 'data': 'deleted'}, status=status.HTTP_204_NO_CONTENT)