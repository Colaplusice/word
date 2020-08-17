# coding=utf-8
"""
@time: 2020-08-17 12:38
@author: colaplusice
@contact: fjl2401@163.com vx:18340071291
"""
# 修复单词

import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'word.settings')
django.setup()
from word_list.models import UserWord, WordList

#
# 1154---1225
user_words = UserWord.objects.filter(list__name='2000.5', id__lte=1225, id__gte=1154).order_by('-id')
new_list = WordList.objects.filter(name='2001.5').first()
print(new_list)
for user_word in user_words:
    print(user_word.word)
    # 移动过去
    UserWord.objects.get_or_create(list=new_list, word=user_word.word)

UserWord.objects.filter(list__name='2000.5', id__lte=1225, id__gte=1154).delete()
