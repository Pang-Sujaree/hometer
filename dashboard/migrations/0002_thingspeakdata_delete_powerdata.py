# Generated by Django 4.2.8 on 2023-12-16 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ThingSpeakData",
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
                ("created_at", models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(name="PowerData",),
    ]