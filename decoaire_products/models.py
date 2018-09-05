# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from decoaire_users.models import *


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    size = models.CharField(max_length=100)
    cloth_type = models.CharField(max_length=100)
   #  url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
	 user = models.ForeignKey(User, on_delete=models.CASCADE)
	 details = models.CharField(max_length=500)
	 quantity = models.IntegerField()
	 is_admin = models.BooleanField()
	 company_client = models.CharField(max_length=500)
	 created_at = models.DateTimeField(auto_now_add=True)
	 updated_at = models.DateTimeField(auto_now=True)

	 def __str__(self):
		 return self.user
