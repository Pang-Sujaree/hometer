# Generated by Django 4.2.8 on 2023-12-15 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PowerData",
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
                ("voltage", models.FloatField()),
                ("current", models.FloatField()),
                ("power", models.FloatField()),
                ("energy", models.FloatField()),
                ("date", models.DateField(auto_now_add=True)),
                ("time", models.TimeField(auto_now_add=True)),
            ],
        ),
    ]