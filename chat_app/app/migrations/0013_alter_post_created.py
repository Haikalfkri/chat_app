# Generated by Django 5.0.2 on 2024-02-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0012_alter_userprofile_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(),
        ),
    ]
