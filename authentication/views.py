from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, GetUserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
# Import Token
from rest_framework.authtoken.models import Token
# Token authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Paginator
from django.core.paginator import Paginator

class Login(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'Status' : False,
                'message' : serializer.errors
            }, status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'Status' : True,
            'message' : 'User login',
            'token' : str(token)
        }, status.HTTP_201_CREATED)
        

class Register(APIView):
    def post(self, request):
        data = request.data 
        serializer = RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'Status' : False,
                'message' : serializer.errors
            }, status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({
            'Status' : True,
            'message' : serializer.data
        }, status.HTTP_201_CREATED)

class TokenAuthenticated(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self, request):
        return Response({
            'Status' : 200,
            'Message' : f"{request.user} is Token Authenticated."
        }, status.HTTP_200_OK)

class GetUserPaginator(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            page = request.GET.get('page', 1)
            page_size = 3
            paginator = Paginator(users, page_size)
            serializer = GetUserSerializer(paginator.page(page), many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'Status' : False,
                'Message' : 'Invalid Page.'
            }, status.HTTP_400_BAD_REQUEST)