from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):

  def create_user(self, data_to_validate):

    first_name = data_to_validate['first_name'],
    # print data_to_validate['first_name']
    last_name = data_to_validate['last_name'],
    email = data_to_validate['email'],
    password = data_to_validate['password']

     # eventually we should hash the password wth bcrypt

class User(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.CharField(max_length=60)
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  objects = UserManager()

