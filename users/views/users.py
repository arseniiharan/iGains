from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from users.serializers.api import users as user_s

User = get_user_model()


@extend_schema_view(
    post=extend_schema(summary='User registration', tags=['Authentication & Authorization']),
)
class RegistrationView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]  # Using AllowAny because of Basic Authentication in DRF and no one except authorized users will have permission to it
    serializer_class = user_s.RegistrationSerializer

@extend_schema_view(
    post=extend_schema(
        request=user_s.ChangePasswordSerializer,
        summary='Password change', tags=['Authentication & Authorization']),
)
class ChangePasswordView(RetrieveUpdateAPIView):
    def post(self, request):
        user = request.user
        serializer = user_s.ChangePasswordSerializer(
            instance=user, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_204_NO_CONTENT)
