"""
@time: 2020-06-23 13:50
@author: colaplusice
@contact: fjl2401@163.com vx:18340071291
"""

from django.urls import path

from word_list import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_words/<int:list_id>', views.list_words, name='list_words'),
    path('/upload_words', views.upload_words, name='upload_words'),
]
