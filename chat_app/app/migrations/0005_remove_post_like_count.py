# Generated by Django 5.0.2 on 2024-02-26 07:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_alter_post_like_count"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="like_count",
        ),
    ]
