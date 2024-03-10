from django.urls import path
from core_1.views import Register, Login, VerifyOtp
urlpatterns = [
    path('public/register', Register.as_view(), name="register"),
    path('public/verify-otp', VerifyOtp.as_view(), name="verifyotp"),
    path('public/login', Login.as_view(), name="login"),
]
