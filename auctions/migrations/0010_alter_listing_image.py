# Generated by Django 4.2.7 on 2023-11-23 04:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0009_alter_listing_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="image",
            field=models.CharField(max_length=350),
        ),
    ]
