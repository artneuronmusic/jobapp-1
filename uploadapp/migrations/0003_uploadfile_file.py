# Generated by Django 5.0 on 2024-01-04 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uploadapp", "0002_uploadfile"),
    ]

    operations = [
        migrations.AddField(
            model_name="uploadfile",
            name="file",
            field=models.FileField(default=False, upload_to="files"),
            preserve_default=False,
        ),
    ]
