# Generated by Django 5.0.2 on 2024-03-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0014_mychats"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mychats",
            name="chat",
            field=models.JSONField(default=dict),
        ),
    ]