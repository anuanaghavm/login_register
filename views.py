from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer

class LoginView(generics.CreateAPIView):
    serializer_class = CustomTokenObtainPairSerializer
