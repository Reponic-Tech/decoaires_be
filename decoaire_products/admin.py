# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product, Image

admin.site.register(Product)
admin.site.register(Image)
# Register your models here.
