from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ParseError
from supabase_py import create_client

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
        )

    def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email=email).exists():
            raise ParseError('User with email like this already exists')
        return email

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        self.create_supabase_user(validated_data['email'], validated_data['password'])
        return user

    def create_supabase_user(self, email, password):
        supabase = create_client('https://waotqiccymmikmwadsdl.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Indhb3RxaWNjeW1taWttd2Fkc2RsIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwMDc2OTkzMywiZXhwIjoyMDE2MzQ1OTMzfQ.572s0u-hpWoMC4ayt9Hhby8XFI8hPzZPGqrZfDcBMuc')
        supabase.auth.sign_up(email, password)


class ChangePasswordSerializer(serializers.Serializer):
    pass
