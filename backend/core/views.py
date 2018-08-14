# this code (in the core app folder) is adapted from the tutorial on Json web token authentication by Daktoa Lillie
# https://medium.com/@dakota.lillie/django-react-jwt-authentication-5015ee00ef9a

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken

@api_view(['GET'])
def current_user(request):
    # Find out who the current user is
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    # this creates a new user

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


