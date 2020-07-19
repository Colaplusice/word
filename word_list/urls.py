"""
@time: 2020-06-23 13:50
@author: colaplusice
@contact: fjl2401@163.com vx:18340071291
"""
from django.conf.urls import url
from django.urls import path

from word_list import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_words/', views.list_words, name='list_words'),
    url(r'^list_words/(?P<list_id>[0-9]+)/$', views.list_words, name='list_words'),
    path('upload_file', views.upload_file, name='upload_file'),
    path('export_list<int:list_id>', views.export_list, name='export_list'),
]
