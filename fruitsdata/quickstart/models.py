from django.db import models

# Create your models here.

class Fruit(models.Model):
    name = models.CharField(max_length = 30)
    taste = models.CharField(max_length = 30)
    benefits = models.CharField(max_length = 30)
    origin = models.CharField(max_length = 30)
    image_url = models.CharField(max_length=100, default='https://github.com/SannatKumar/django_images/blob/master/django_images/mango.jpg')
