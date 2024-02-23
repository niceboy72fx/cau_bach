# Generated by Django 4.2.6 on 2023-10-26 10:50
import uuid
from typing import Any

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: list[Any] = []

    operations = [
        migrations.CreateModel(
            name="Otp",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("target", models.CharField(max_length=128)),
                (
                    "type",
                    models.IntegerField(choices=[(1, "Signup"), (2, "Reset password")]),
                ),
                (
                    "source",
                    models.IntegerField(
                        choices=[(1, "Email"), (2, "Mobile")], default=1
                    ),
                ),
                ("code", models.CharField(max_length=64)),
                ("fail_checks", models.IntegerField(default=0)),
                ("resend_expired_at", models.DateTimeField()),
                (
                    "ips",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.GenericIPAddressField(),
                        default=list,
                        size=None,
                    ),
                ),
                ("verified_at", models.DateTimeField(default=None, null=True)),
                ("expired_at", models.DateTimeField()),
                ("extra_data", models.JSONField(blank=True, default=dict)),
            ],
            options={
                "db_table": "otps",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="TrustedTarget",
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
                ("target", models.CharField(max_length=128, unique=True)),
            ],
            options={
                "db_table": "trusted_targets",
                "ordering": ["-id"],
            },
        ),
    ]
