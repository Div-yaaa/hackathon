from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = ('name', 'email', 'password')


class ChangePasswordSerializer(serializers.Serializer):

    class Meta:
        model = Sales
        old_password = serializers.CharField(required=True)
        new_password = serializers.CharField(required=True)


class DeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Developer
        fields = '__all__'


class SalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = ['full_name', 'email']


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class CilentSerializer(serializers.ModelSerializer):
    course = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Cilent
        fields = '__all__'
        depth = 1
