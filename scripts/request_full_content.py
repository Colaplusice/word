"""
@time: 2020-07-18 10:46
@author: colaplusice
@contact: fjl2401@163.com vx:18340071291
"""
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'word.settings')

django.setup()

from word_list.models import Word
from utils import request_translate

words = Word.objects.all()
for word in words:
    print(word.data, type(word.data))
    # continue
    if word.data == {}:
        data = request_translate(word.content)
        if data['msg'] == 'SUCCESS':
            word.data = data
            word.save()
