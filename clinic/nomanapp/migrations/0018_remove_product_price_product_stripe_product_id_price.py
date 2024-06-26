# Generated by Django 5.0.6 on 2024-05-31 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nomanapp", "0017_product"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="price",
        ),
        migrations.AddField(
            model_name="product",
            name="stripe_product_id",
            field=models.CharField(default="your_default_value_here", max_length=100),
        ),
        migrations.CreateModel(
            name="Price",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "stripe_price_id",
                    models.CharField(default="your_default_value_here", max_length=100),
                ),
                ("price", models.IntegerField(default=0)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nomanapp.product",
                    ),
                ),
            ],
        ),
    ]
