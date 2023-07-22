from rest_framework import serializers
from .models import CustomUserModel
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ('id', 'email')

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = '__all__'

        extra_kwargs = {
            'password': {'required': True}
        }

    def validate(self, attrs):
        email = attrs.get('email', '').strip().lower()

        if CustomUserModel.objects.filter(email=email).exists():
            raise serializers.ValidationError('User already exist.')
        return attrs
    
    def create(self, validate_data):
        user = CustomUserModel.objects.create_user(**validate_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type':'password'},trim_whitespace = False)   
    def validate(self, attrs):
        email = attrs.get('email').lower()
        password = attrs.get('password')    
        if not email or not password:
            raise serializers.ValidationError('Please Provide both email and password')

        if not CustomUserModel.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email Does not Exist')

        user = authenticate(request=self.context.get('request'), email = email, password = password)    
        if not user:
                raise serializers.ValidationError('Wrong Credential')   
        attrs['user'] = user
        return attrs