# Generated by Django 5.0 on 2023-12-19 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_jobpost_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobpost",
            name="slug",
            field=models.SlugField(max_length=40, null=True, unique=True),
        ),
    ]
