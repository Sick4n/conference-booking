from django.urls import path
from core_1.views import Register
urlpatterns = [
    path('public/regiter', Register.as_view(), name="register"),
    path('public/get-new-otp', Register.as_view(), name="register")
]
