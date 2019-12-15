# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-15 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=60)),
                ('doctor', models.IntegerField()),
                ('patient', models.IntegerField()),
                ('medicCenter', models.IntegerField()),
                ('responsible', models.IntegerField()),
                ('appointmentDate', models.TimeField()),
                ('indications', models.CharField(max_length=60)),
                ('diagnosis', models.CharField(max_length=60)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('skullCircumference', models.IntegerField()),
            ],
        ),
    ]