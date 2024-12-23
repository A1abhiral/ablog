# Generated by Django 5.1.1 on 2024-09-30 08:25

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_profile_x_url_profile_facebook_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
