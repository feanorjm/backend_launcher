# Generated by Django 3.0 on 2019-12-09 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_launcher', '0009_app_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='images',
        ),
    ]
