# Generated by Django 5.1.1 on 2024-10-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0016_alter_post_header_image_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
