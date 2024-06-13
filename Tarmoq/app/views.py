from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Profile, Friend, Message
from .serializers import UserSerializer, ProfileSerializer, FriendSerializer, MessageSerializer
# Create your views here.




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer



class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer