from django.shortcuts import render, reverse, redirect

from word_list.models import WordList, UserWord


# Create your views here.
def user_login():
    pass

def index(request):
    all_list = WordList.objects.all()
    return render(request, 'index.html', {'all_list': all_list})


def list_words(request, list_id):
    print_type = request.GET.get('type', '1')
    print(print_type)
    list_words = WordList.objects.get(id=list_id)
    allword=list_words.userword_set.all()
    # for w in allword:
        # print(w.word.content)
    return render(request, 'list_words.html', {'list_words': list_words, 'type': print_type})


def read_txt(filename):
    userowrd = UserWord.objects.first()
    # userowrd.list
    # with
    pass


def upload_words(request):
    # file=request.POST.fi
    return redirect(reverse('list_words'))
    pass


def get_translate():
    pass
