# Generated by Django 5.0.2 on 2024-03-08 10:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0015_alter_mychats_chat"),
    ]

    operations = [
        migrations.DeleteModel(
            name="myChats",
        ),
    ]