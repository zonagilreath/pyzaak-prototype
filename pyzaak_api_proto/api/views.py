from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers
from . import permissions


class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "username"
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsUserOrReadOnly,)


class GameList(generics.ListAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer


class SideDeckDetail(generics.RetrieveUpdateAPIView):
    lookup_field = 'user'
    queryset = models.SideDeck.objects.all()
    serializer_class = serializers.SideDeckSerializer
    permission_classes = (permissions.IsOwnerOrReadOnly,)
