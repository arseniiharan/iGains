from django.contrib.auth import get_user_model

User = get_user_model()


# Creating email authentication
class EmailAuthBackend:
    supports_object_permission = True
    supports_anonymous_user = True
    supports_inactive_user = True

    def get_user(self, user_id):  # finding the user by his id
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExicst:
            return None

    def authenticate(self, request, email=None, password=None):  # trying to auth the user by getting his email
        try:                                                     # and comparing his password with password in db
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExicst:
            return None
