from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('name', 'email', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)

        if password is not None:
            user.set_password(password)
            user.is_active = True
        user.save()
        return user


class DeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Developer
        fields = '__all__'


class SalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class CilentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cilent
        fields = '__all__'