# Generated by Django 5.0.6 on 2024-06-27 10:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MyApp",
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
                ("service_icon", models.CharField(max_length=50)),
                ("service_title", models.CharField(max_length=50)),
                ("service_desp", models.TextField()),
            ],
        ),
    ]
