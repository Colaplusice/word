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
import time
import random

words = Word.objects.all()
for word in words:
    if word.data == {}:
        print('requesting word:'.format(word.content))
        time.sleep(random.randint(1, 3))
        data = request_translate(word.content)
        if data['msg'] == 'SUCCESS':
            word.data = data
            word.save()
