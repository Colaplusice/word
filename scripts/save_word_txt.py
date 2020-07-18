"""
@time: 2020-07-01 23:48
@author: colaplusice
@contact: fjl2401@163.com vx:18340071291
"""
"""
@time: 2020-06-26 16:13
@author: colaplusice
@contact: fjl2401@163.com vx:18340071291
"""
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'word.settings')

django.setup()

from word_list.models import Word

words = Word.objects.all()
words = set(words)

with open('word.txt', 'w')as opener:
    for word in words:
        opener.write(word.content + '\n')
