# Generated by Django 3.0.3 on 2020-03-23 21:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('turf_booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turf',
            name='password',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slot',
            name='timing',
            field=models.TimeField(default=datetime.datetime(2020, 3, 23, 21, 23, 22, 181611, tzinfo=utc)),
        ),
    ]