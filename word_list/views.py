from django.shortcuts import render

from word_list.models import WordList


# Create your views here.

def index(request):
    all_list = WordList.objects.all()
    return render(request, 'index.html', {'all_list': all_list})


def list_words(request, list_id):
    list_words = WordList.objects.get(id=list_id)
    return render(request, 'list_words.html', {'list_words': list_words})
