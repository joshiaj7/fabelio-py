# Generated by Django 3.0.3 on 2020-03-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("pricing_app", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.CharField(default="", max_length=1000),
        )
    ]
