# Generated by Django 5.0.7 on 2024-07-14 02:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="id",
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]