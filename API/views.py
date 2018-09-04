from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics


# Create your views here.
class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
