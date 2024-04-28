from django.contrib.auth.models import User
from rest_framework import serializers

class UserSignupSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    is_staff = serializers.BooleanField(default=False, write_only=True)  # Allow specifying is_staff, default to False

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_confirmation', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True, 'allow_blank': False}
        }

    def validate_email(self, value):
        # Validate that the email is unique
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return value

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({"password_confirmation": "Password and confirmation do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation', None)  # Remove confirmation from data since it's not needed for user creation
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            is_staff=validated_data.get('is_staff', False)  # Use the provided is_staff value, or False as default
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
