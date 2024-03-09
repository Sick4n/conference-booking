from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from core_1.utils import generate_otp, email_manager
from django.contrib import messages
from django.utils.safestring import mark_safe

class Register(TemplateView):
    """
    View for user registration.

    Handles both GET and POST requests for user registration form submission.
    """

    template_name = "core_1/register.html"
    error_page = "core_1/opps_404.html"
    otp_verify_page = "core_1/otp_verify.html"

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for user registration.

        Args:
            request (HttpRequest): The request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponse: Response based on registration status.
        """
        # Retrieve form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirmpassword')

        # Check if email and password match confirmation
        if email and password == confirm_pass:
            # Create user instance
            user = User.objects.create_user(username=username, email=email, password=password)

            # Generate OTP
            otp = generate_otp()

            # Email verification code to user
            subject = f"{otp} is your Account verification code"
            message = f"Hi {username}! <br> We received a request to create your account. <br> Enter the one-time code to verify your account:<br> <b>{otp}</b>"

            # Send email
            email_manager(user, subject, message)
            
            return render(request, self.otp_verify_page)
            
        elif email is None:
            # If email is not provided, show error message and redirect to registration page
            messages.error(request, "Email not provided.")
            return redirect("register")
        else:
            # If passwords don't match, show error message and redirect to registration page
            messages.error(request, "Passwords do not match.")
            return redirect("register")
    
    def get(self, request, *args, **kwargs):
        """
        Handle GET requests for user registration.

        Args:
            request (HttpRequest): The request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponse: Rendered registration template.
        """
        # Render the registration template
        return render(request, self.template_name)
