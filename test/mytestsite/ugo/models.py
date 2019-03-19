from django.db import models

# Create your models here.
class count(models.Model):
    turl = models.CharField(max_length = 255)
    surl = models.CharField(max_length = 20)
    c = models.IntegerField()
    z = 123