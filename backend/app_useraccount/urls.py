from django.urls import path
from .views import RegisterView, OTPVerifyView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='api_register'),
    path('verify-otp/', OTPVerifyView.as_view(), name='api_verify_otp'),
]
