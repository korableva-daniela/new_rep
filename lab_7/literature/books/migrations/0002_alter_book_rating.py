# Generated by Django 5.0.4 on 2024-04-05 10:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="rating",
            field=models.IntegerField(
                blank=True,
                choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                default=0,
                verbose_name="Оценка",
            ),
        ),
    ]
