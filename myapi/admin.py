# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Hero, Appointments

admin.site.register(Hero)
admin.site.register(Appointments)

# Register your models here.
