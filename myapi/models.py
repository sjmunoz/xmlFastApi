# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Appointments(models.Model):
    alias = models.CharField(max_length=60)
    doctor = models.IntegerField()
    patient = models.IntegerField()
    medicCenter = models.IntegerField()
    responsible = models.IntegerField()
    appointmentDate = models.TimeField() 
    indications = models.CharField(max_length=60)
    diagnosis = models.CharField(max_length=60)
    weight = models.IntegerField()
    height = models.IntegerField()
    skullCircumference = models.IntegerField()

    def __str__(self):
        return self.diagnosis

