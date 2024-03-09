# Generated by Django 5.0.3 on 2024-03-08 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meetups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('description', models.TextField(db_index=True)),
                ('start_time', models.TimeField(auto_now_add=True)),
                ('end_time', models.TimeField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('conference_slug', models.SlugField(default='', unique=True)),
                ('is_overed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('profile', models.ImageField(blank=True, db_index=True, null=True, upload_to='profile/images')),
                ('first_name', models.CharField(db_index=True, default='', max_length=100, null=True)),
                ('last_name', models.CharField(db_index=True, default='', max_length=100, null=True)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('username', models.CharField(db_index=True, max_length=100, unique=True)),
                ('otp', models.PositiveIntegerField(db_index=True, null=True)),
                ('otp_limit', models.IntegerField(db_index=True, null=True)),
                ('otp_delay', models.TimeField(auto_now=True, db_index=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('last_login', models.DateTimeField(db_index=True, default=None, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('password', models.CharField(db_index=True, default=None, max_length=200)),
                ('groups', models.ManyToManyField(blank=True, related_name='user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='user_permissions', to='auth.permission')),
                ('r_conference', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='conferences', to='core_1.meetups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]