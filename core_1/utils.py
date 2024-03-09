from django.core.mail import send_mail
from django.conf import settings
from random import randint


def email_manager(user, **kwargs):
    subject = kwargs.get("subject")
    message = kwargs.get("message")
    
    try:
        send_mail(subject, message, settings.EMAIL_HOST, user.email)
        return True
    except:
        return False

def generate_otp():
    otp = randint(100000, 999999)

    return otp