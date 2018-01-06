from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    publish_time = models.DateTimeField()
    content = models.TextField(max_length=5000)
    image = models.ImageField()
