# Generated by Django 5.1.1 on 2024-09-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0011_alter_post_header_image_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]
