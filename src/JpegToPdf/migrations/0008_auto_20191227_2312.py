# Generated by Django 2.0.7 on 2019-12-27 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JpegToPdf', '0007_auto_20191227_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pdf',
            old_name='file',
            new_name='image_file',
        ),
        migrations.RemoveField(
            model_name='pdf',
            name='cover',
        ),
    ]
