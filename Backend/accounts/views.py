from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

User = get_user_model()
from .serializers import SignUpSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class SignUpView(CreateAPIView):
    queryset = User.objects.all() #get all users
    serializer_class = SignUpSerializer 
    permission_classes = [AllowAny]

    def perform_create(self,serializer):
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            User.objects.create_user(username=username, password=password) #create_user is built in DRF to hash sensitive fields (passwords) 