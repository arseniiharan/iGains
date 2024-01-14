from django.urls import path, include
from users.views import users

urlpatterns = [
    path('user/reg/', users.RegistrationView.as_view(), name='reg'),
]