# Generated by Django 4.2.15 on 2024-08-25 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_disease_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="medicationtype",
            options={"ordering": ["name"]},
        ),
    ]