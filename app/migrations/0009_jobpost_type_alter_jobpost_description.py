# Generated by Django 5.0 on 2024-01-05 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_skills_jobpost_skills"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobpost",
            name="type",
            field=models.CharField(
                choices=[("Full Time", "Full Time"), ("Part Time", "Full Time")],
                default="Full Time",
                max_length=200,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="jobpost",
            name="description",
            field=models.TextField(max_length=200),
        ),
    ]
