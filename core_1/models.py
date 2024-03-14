from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
from core_1.manager import CustomUserManager
from django.utils.text import slugify
import uuid


# Create your models here.
class Meetup(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    conference_slug = models.SlugField(unique=True)
    description = models.TextField(db_index=True)
    start_time = models.TimeField(auto_now_add=True)
    end_time = models.TimeField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_overed = models.BooleanField(default=False)
    people = models.ManyToManyField('User', related_name='attended_meetups')
    place = models.CharField(max_length=100, db_index=True, null=True)

    def save(self, *args, **kwargs):
        # Generate a unique slug based on the title
        if not self.conference_slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while Meetup.objects.filter(conference_slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{uuid.uuid4().hex[:6]}-{counter}"
                counter += 1
            self.conference_slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class User(AbstractUser):
    profile = models.ImageField(upload_to="usr/profile", null=True, db_index=True)
    first_name = models.CharField(max_length=100, default="", null=True, db_index=True)
    last_name = models.CharField(max_length=100, default="", null=True, db_index=True)
    r_conference = models.ForeignKey(Meetup, related_name='conferences', null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, db_index=True)
    phone_no = models.BigIntegerField(db_index=True, null=True)
    username = models.CharField(null=False, max_length=100, unique=True, db_index=True)
    otp = models.PositiveIntegerField(null=True, db_index=True)
    otp_limit = models.IntegerField(null=True, db_index=True)
    otp_delay = models.TimeField(auto_now=True, db_index=True)
    date_joined = models.DateTimeField(auto_now_add=True, db_index=True)
    last_login = models.DateTimeField(default=None, null=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    password = models.CharField(max_length=200, db_index=True, default=None)
    active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    groups = models.ManyToManyField(Group, related_name='user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions', blank=True)


class Contact(models.Model):
    full_name = models.CharField(max_length=100, null=True, db_index=True)
    email = models.EmailField(db_index=True)
    issue = models.TextField(db_index=True)
    
