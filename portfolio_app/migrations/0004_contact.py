# Generated by Django 5.1.1 on 2024-12-10 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0003_certificate_skill"),
    ]

    operations = [
        migrations.CreateModel(
            name="contact",
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
                ("GitHub", models.URLField(blank=True, null=True)),
                ("LinkedIn", models.URLField(blank=True, null=True)),
                ("Whatsapp", models.URLField(blank=True, null=True)),
                ("Email", models.EmailField(max_length=254)),
            ],
        ),
    ]
