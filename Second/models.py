from django.utils import timezone

from django.db import models

# Create your models here.

# '''
# 文件记录
# '''
# class FileInfo(models.Model):
#     file_name = models.CharField(max_length=500)
#     file_size = models.DecimalField(max_digits=10, decimal_places=0)
#     file_path = models.CharField(max_length=500)
#     upload_time = models.DateTimeField(default=timezone.now())
class IMG(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

class SF(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

class Bsqr(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

class Fzm(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
class Fbm(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
class Bzm(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
class Bbm(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)