from django.urls import path
from core_1.views import Register, Login, VerifyOtp, about, contact
urlpatterns = [
    path('public/register', Register.as_view(), name="register"),
    path('public/login', Login.as_view(), name="login"),
    path('public/verify-otp', VerifyOtp, name="verifyotp"),
    path('public/company/about', about, name="about"),
    path('public/company/contact', contact, name="contact"),
]
