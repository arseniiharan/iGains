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
        try:
            supabase = create_client('https://waotqiccymmikmwadsdl.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Indhb3RxaWNjeW1taWttd2Fkc2RsIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwMDc2OTkzMywiZXhwIjoyMDE2MzQ1OTMzfQ.572s0u-hpWoMC4ayt9Hhby8XFI8hPzZPGqrZfDcBMuc')
            response = supabase.auth.sign_up(email, password)

            if response.status_code == 200:
                # Successful registration in Supabase
                return response.json()
            else:
                raise ParseError(f"Supabase registration failed: {response.content}")

        except Exception as e:
            raise ParseError(f"Supabase registration failed: {str(e)}")


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('old_password', 'new_passwrod')

    def validate(self, attrs):
        user = self.instance
        old_password = attrs.pop('old_password')
        if not user.check_password(old_password):
            raise ParseError('Old password doesn\'t match')
        return attrs

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def update(self, instance, validated_data):
        password = validated_data.pop('new_password')
        instance.set_password(password)
        instance.save()
        return instance

