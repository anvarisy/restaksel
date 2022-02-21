from django.db import models

# Create your models here.
class Santri(models.Model):
    nis = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=60)
    password = models.TextField()
    name = models.CharField(max_length=36,null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)
    address = models.TextField(null=True,blank=True)