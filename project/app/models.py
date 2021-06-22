from django.db import models
from django import forms


# Create your models here.
class blog(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=100000000)
    dat = models.DateTimeField(auto_now_add=True)
    upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# class ch(models.Model):
#     data = blog.objects.only("name")
#     names = []
#     for i in data:
#         a = (str(i), str(i))
#         names.append(a)
#     names = tuple(names)
#     name=models.CharField(max_length=100, choices=names)
