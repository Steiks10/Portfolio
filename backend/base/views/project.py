from ..models import Project
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from ..models import Project
from rest_framework.response import Response
from ..serializers import ProjectSerializer
from rest_framework.decorators import api_view, action

@api_view(['GET', 'POST', 'PUT'])
def project_general(request):
    query = Project.objects.all()
    if request.method == 'GET':
        serializer = ProjectSerializer(query, many = True)
        return Response({'status': 200, 'data': serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        serializer = ProjectSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

@api_view(['GET','PUT', 'PATCH', 'DELETE'])
def project_detail(request, pk=None):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    # elif request.method == 'PUT':
    #     data = request.data
    #     serializer = ProjectSerializer(obj, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

# def project_detail(request, pk):
