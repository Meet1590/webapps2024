# Generated by Django 5.0.4 on 2024-05-01 05:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payapp", "0002_alter_transaction_source_user_email"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="currency",
            field=models.CharField(
                choices=[
                    ("GBP", "British Pound"),
                    ("USD", "US Dollar"),
                    ("EUR", "Euro"),
                ],
                default="GBP",
                max_length=3,
            ),
        ),
        migrations.CreateModel(
            name="PaymentRequest",
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("accepted", "Accepted"),
                            ("rejected", "Rejected"),
                        ],
                        default="pending",
                        max_length=10,
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_requests",
                        to=settings.AUTH_USER_MODEL,
                        to_field="email",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_requests",
                        to=settings.AUTH_USER_MODEL,
                        to_field="email",
                    ),
                ),
            ],
        ),
    ]