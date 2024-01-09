# Generated by Django 5.0 on 2023-12-19 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_author_jobpost_author"),
    ]

    operations = [
        migrations.CreateModel(
            name="Skills",
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
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name="jobpost",
            name="skills",
            field=models.ManyToManyField(to="app.skills"),
        ),
    ]
