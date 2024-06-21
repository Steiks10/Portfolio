from ..models import Skill
from rest_framework import viewsets, status
from ..serializers import SkillSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
class SkillViewSet(viewsets.ViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    query = Skill.objects.all()
    serializer_class = SkillSerializer

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
        company = get_object_or_404(self.query, pk=pk)
        serializer = self.serializer_class(company)
        return Response({'status': 201, 'data': serializer.data}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        company = get_object_or_404(self.query, pk=pk)
        serializer = self.serializer_class(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def partial_update(self, request, pk=None):
        company = get_object_or_404(self.query, pk=pk)
        serializer = self.serializer_class(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)