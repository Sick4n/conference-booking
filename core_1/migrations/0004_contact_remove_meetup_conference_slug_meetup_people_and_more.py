# Generated by Django 5.0.3 on 2024-03-08 20:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_1', '0003_rename_meetups_meetup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(db_index=True, max_length=100, null=True)),
                ('email', models.EmailField(db_index=True, max_length=254)),
                ('issue', models.TextField(db_index=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='meetup',
            name='conference_slug',
        ),
        migrations.AddField(
            model_name='meetup',
            name='people',
            field=models.ManyToManyField(related_name='attended_meetups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(db_index=True, null=True, upload_to='usr/profile'),
        ),
        migrations.AlterField(
            model_name='user',
            name='r_conference',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conferences', to='core_1.meetup'),
        ),
    ]