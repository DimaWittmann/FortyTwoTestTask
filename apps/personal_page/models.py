from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    bio = models.TextField(default='')
    email = models.EmailField(max_length=254)
    jabber = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    other_contacts = models.TextField(default='')
