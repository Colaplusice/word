from django.db import models


# Create your models here.

class Word(models.Model):
    content = models.CharField(max_length=32)
