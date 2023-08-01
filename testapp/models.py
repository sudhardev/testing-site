from django.db import models

class test(models.Model):

    title = models.CharField(max_length=100)

    subtitle = models.CharField(max_length=100)

    links = models.CharField(max_length=100,null=True)

    comment = models.TextField(max_length=1000,null=False)
# Create your models here.
