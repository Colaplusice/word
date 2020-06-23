from django.db import models


# Create your models here.

class WordList(models.Model):
    name = models.CharField(verbose_name='单词组名', max_length=255)

    def __str__(self):
        return self.name


class Word(models.Model):
    list = models.ManyToManyField(WordList, verbose_name='列表名')
    content = models.CharField(max_length=32, unique=True)
