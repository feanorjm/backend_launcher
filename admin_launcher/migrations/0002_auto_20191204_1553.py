# Generated by Django 3.0 on 2019-12-04 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_launcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to='media/backgrounds'),
        ),
    ]
