from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    # Private method to create user example
    def _create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field must be set')  # checking if email not empty

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)  # using email for user identification
        user.email = email
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Public method to create users
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)

        return self._create_user(email, password, **extra_fields)

    # Public method to create superuser
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self._create_user(email, password, **extra_fields)
