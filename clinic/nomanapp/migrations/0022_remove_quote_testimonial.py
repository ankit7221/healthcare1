# Generated by Django 5.0.6 on 2024-06-02 13:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("nomanapp", "0021_appointment_user_alter_appointment_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quote",
            name="testimonial",
        ),
    ]
