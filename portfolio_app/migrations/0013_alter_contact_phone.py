# Generated by Django 5.1.1 on 2024-12-29 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0012_education"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="PHONE",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
