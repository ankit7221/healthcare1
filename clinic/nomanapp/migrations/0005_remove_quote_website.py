# Generated by Django 5.0.6 on 2024-05-25 18:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("nomanapp", "0004_quote"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quote",
            name="Website",
        ),
    ]