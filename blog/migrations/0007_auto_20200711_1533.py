# Generated by Django 3.0.6 on 2020-07-11 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200711_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_posted',
            new_name='date_published',
        ),
    ]
