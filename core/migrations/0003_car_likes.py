# Generated by Django 4.1 on 2024-08-31 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_car_brand_alter_car_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="likes",
            field=models.IntegerField(default=0),
        ),
    ]