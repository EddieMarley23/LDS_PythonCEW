# Generated by Django 4.1 on 2024-08-31 22:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_car_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="photo",
            field=models.ImageField(
                upload_to="",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        ["png", "jpg", "jpeg"]
                    )
                ],
            ),
        ),
    ]
