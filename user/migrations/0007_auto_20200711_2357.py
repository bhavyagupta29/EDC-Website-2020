# Generated by Django 3.0.7 on 2020-07-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200711_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='cgpa',
            field=models.FloatField(default=0),
        ),
    ]
