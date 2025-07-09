from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from apps.users.models import Users
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'username': {'required': True},
            'is_active': {'required': False}  # optional override
        }

    def validate_password(self, value):
        """
        Validate strong password rules:
        - At least 8 characters
        - At least 1 uppercase, 1 lowercase, 1 digit, 1 special character
        """
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r'\d', value):
            raise serializers.ValidationError("Password must contain at least one digit.")
        if not re.search(r'[^\w\s]', value):
            raise serializers.ValidationError("Password must contain at least one special character.")
        return make_password(value)

    def validate_email(self, value: str):
        """
        Normalize email to lowercase.
        """
        return value.lower()

    def validate(self, attrs: dict):
        """
        Cross-field validations.
        """
        if attrs.get('username') == attrs.get('email'):
            raise serializers.ValidationError("Username and email cannot be the same.")
        return attrs
