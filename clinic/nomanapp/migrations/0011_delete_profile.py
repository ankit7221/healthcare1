# Generated by Django 5.0.6 on 2024-05-30 05:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("nomanapp", "0010_remove_profile_profile_photo_profile_profile_picture"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
