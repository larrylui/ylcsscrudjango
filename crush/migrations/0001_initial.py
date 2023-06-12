# Generated by Django 4.1.7 on 2023-04-08 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("class_no", models.CharField(max_length=2)),
                ("student_no", models.IntegerField()),
                ("unique_id", models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Crush",
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
                ("matched", models.BooleanField(default=False)),
                (
                    "crush",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="admirers",
                        to="crush.user",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="crushes",
                        to="crush.user",
                    ),
                ),
            ],
        ),
    ]
