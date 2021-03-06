# Generated by Django 3.0.4 on 2020-05-31 21:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Turf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.TextField()),
                ('password', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timing', models.TimeField(default=datetime.datetime(2020, 5, 31, 21, 13, 49, 972511, tzinfo=utc))),
                ('date', models.DateField()),
                ('book_timing', models.DateTimeField(auto_now_add=True)),
                ('turf', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='turf_booking.Turf')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='turf_booking.Bookie')),
            ],
        ),
    ]
