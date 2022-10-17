from django.db import models

# Create your models here.
class Yyzz_first(models.Model):
    username = models.CharField(max_length=200)
    img = models.ImageField(upload_to='img/username')