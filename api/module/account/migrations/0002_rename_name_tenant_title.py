# Generated by Django 4.2.6 on 2023-10-26 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tenant",
            old_name="name",
            new_name="title",
        ),
    ]
