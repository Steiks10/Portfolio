from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework import viewsets, status
from ..serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token



class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data = data)
        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors
            }, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({'status': True, 'message': 'user created'}, status.HTTP_201_CREATED)



class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if not serializer.is_valid():
            return Response({
               'status': False,
               'message': serializer.errors
            }, status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=serializer.data['username'],
                            password=serializer.data['password'])
        if not user:
            return Response({
                'status': False,
                'message': 'User not found'
            }, status.HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'status': True, 'message': 'User Logged', 'token': str(token)}, status.HTTP_202_ACCEPTED)