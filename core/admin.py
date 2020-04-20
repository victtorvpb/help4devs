# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Dev, JobName

# Register your models here.
admin.site.register(Dev)
admin.site.register(JobName)