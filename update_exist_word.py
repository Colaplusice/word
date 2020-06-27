"""
@time: 2020-06-26 16:13
@author: colaplusice
@contact: fjl2401@163.com vx:18340071291
"""
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'word.settings')

django.setup()

from word_list.models import Word, get_translate

words = Word.objects.filter(translate='翻译')

for word in words:
    word.translate = get_translate(word.content)
    word.save()
