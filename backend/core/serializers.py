# this code (in the core app folder) is adapted from the tutorial on Json web token authentication by Daktoa Lillie
# https://medium.com/@dakota.lillie/django-react-jwt-authentication-5015ee00ef9a

from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # regular serializer for users already registered

    class Meta:
        # tells serializer which model to use, what fields are needed from it
        model = User
        fields = ('username',)




class UserSerializerWithToken(serializers.ModelSerializer):
    # A class for when a user signs up/registers for first time (so creates token)

    # define fields that get serialized
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        # this creates a new json web token (jwt), then returns it
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        # change/override the create method inherited from serializer
        # this defines how instances of class being serialized (ie User) are created.
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        # set_password method applied to instance of class user
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        # tells serializer which model to use, what fields are needed from it
        model = User
        fields = ('token', 'username', 'password')