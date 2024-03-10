from django.core.mail import send_mail
from django.conf import settings
from random import randint


def email_manager(user, subject, message):
    """
    Sends an email to the specified user.

    Args:
        user: The user object to whom the email will be sent.
        **kwargs: Additional keyword arguments.
            subject (str): The subject of the email.
            message (str): The content of the email.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    
    try:
        send_mail(subject, message, settings.EMAIL_HOST, [user.email])
        return True
    except Exception as e:
        # Log the exception or handle it appropriately
        return False

def generate_otp():
    """
    Generates a random one-time password (OTP).

    Returns:
        int: The generated OTP.
    """
    otp = randint(100000, 999999)
    return otp