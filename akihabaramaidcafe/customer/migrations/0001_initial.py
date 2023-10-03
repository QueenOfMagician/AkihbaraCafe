# Generated by Django 4.1.7 on 2023-09-16 08:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
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
                ("nama_menu", models.CharField(max_length=100)),
                ("stok", models.IntegerField(default=0)),
                ("deskripsi", models.TextField()),
            ],
        ),
    ]
