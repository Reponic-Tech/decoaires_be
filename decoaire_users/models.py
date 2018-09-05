from __future__ import unicode_literals
from django.db import models
# Create your models here.


class User(models.Model):
    admin = models.CharField(max_length=100)
    employees = models.CharField(max_length=100)
    app_users = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class AppUser(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    name_company = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Company(models.Model):
	name = models.CharField(max_length=100)
	website = models.CharField(max_length=100)
	creator = models.ForeignKey(Admin, on_delete=models.CASCADE)
	from_field = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
