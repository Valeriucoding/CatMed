# Generated by Django 4.2.15 on 2024-08-25 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="disease",
            options={"ordering": ["name"]},
        ),
    ]
