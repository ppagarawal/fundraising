# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Campaign, Supporter
# Register your models here.

admin.site.register(Campaign)
admin.site.register(Supporter)