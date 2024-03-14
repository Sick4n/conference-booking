from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from core_1.utils import generate_otp, email_manager
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
import datetime

User = get_user_model()


class Register(TemplateView):
    """
    View for user registration.

    Handles both GET and POST requests for user registration form submission.
    """

    template_name = "core_1/signup.html"
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
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirm_password')

        # Check if email and password match confirmation
        if email and password == confirm_pass:
            # Create user instance
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, username=username, email=email, password=password)

            # Generate OTP
            otp = generate_otp()

            # Email verification code to user
            subject = f"{otp} is your Account verification code"
            message = f"Hi {username}!\n\nWe received a request to create your account.\n\nEnter the one-time code to verify your account:\n\n{otp}"
            user.otp = otp
            user.save()
            # Send email
            email_manager(user, subject, message)

            return render(request, self.otp_verify_page, {"email": email})

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


class Login(TemplateView):

    template_name = "core_1/login.html"
    otp_verify_page = "core_1/otp_verify.html"
    index_template = 'index.html'

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)

        if user:

            if not user.is_verified:
                
                return render(request, self.otp_verify_page, {"email": email})
            if not user.active:
                messages.error(
                    request, 'Sorry your account is temporary disabled, Contact with our team.')
                return redirect('login')

            login(request, user)
            return render(request, self.template_name)

        messages.error(request, 'Invalid credential.')
        return redirect('login')
    
    def get(self, request):

        return render(request, self.template_name)

def VerifyOtp(request):
    if request.method == "POST":
        email = request.POST.get('email')
        otp = request.POST.get('otp')
       
        if email and otp:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, 'User with this email does not exist.')
                return redirect('verifyotp')

            current_time = datetime.datetime.now().time()

            if str(user.otp) == otp:  
                if current_time.minute - user.otp_delay.minute > 5:
                    messages.error(request, 'Otp Expired.')
                    return redirect('verifyotp')
                user.is_verified = True
                user.save()
                
                login(request, user)
                return redirect('Home')
            else:
                messages.error(request, 'Invalid Otp.')
                return redirect('verifyotp')
        else:
            messages.error(request, 'Credentials not provided.')
            return redirect('verifyotp')
    # Add a return statement in case the request method is not POST
    messages.error(request, 'Invalid request.')
    return redirect('verifyotp')


# RENDER FUNCTIONS
def about(request):
    return render(request, 'core_1/About.html')

# RENDER FUNCTIONS
def contact(request):
    return render(request, 'core_1/contact.html')