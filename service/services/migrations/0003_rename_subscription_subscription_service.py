# Generated by Django 5.0.7 on 2024-07-30 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0002_alter_plan_discount_percent"),
    ]

    operations = [
        migrations.RenameField(
            model_name="subscription",
            old_name="subscription",
            new_name="service",
        ),
    ]
