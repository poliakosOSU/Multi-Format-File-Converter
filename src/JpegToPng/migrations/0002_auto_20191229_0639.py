# Generated by Django 2.0.7 on 2019-12-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JpegToPng', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='png',
            name='image_file',
            field=models.FileField(null=True, upload_to='JpegToPng/converted/'),
        ),
    ]