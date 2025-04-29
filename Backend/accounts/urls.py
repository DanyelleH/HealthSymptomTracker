from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import SignUpView
urlpatterns = [
    path("login", obtain_auth_token), # get-token
    path("signup", SignUpView.as_view()),
]