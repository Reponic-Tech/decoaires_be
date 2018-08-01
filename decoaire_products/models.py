# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.DateTimeField('date published')


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    route = models.CharField(max_length=200)    
