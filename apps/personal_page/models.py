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
    image = models.ImageField(upload_to='images/', default='images/no-img.jpg')


class RequestLog(models.Model):
    body = models.TextField(null=True)
    get = models.TextField(null=True)
    post = models.TextField(null=True)
    path = models.CharField(max_length=255, null=True)
    method = models.TextField(max_length=10, null=True)
    encoding = models.TextField(max_length=255, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ('-timestamp', )
