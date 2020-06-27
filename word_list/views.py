from django.shortcuts import render, reverse, redirect

from word_list.models import WordList, UserWord


# Create your views here.
def user_login():
    pass


def index(request):
    all_list = WordList.objects.order_by('-created')
    return render(request, 'index.html', {'all_list': all_list})


def list_words(request, list_id=None):
    # 所有单词
    word_list = []
    title = '所有单词'
    if list_id is None:
        lists = WordList.objects.all()
        for li in lists:
            word_list.extend(li.userword_set.all())
    else:
        li = WordList.objects.get(id=list_id)
        word_list.extend(li.userword_set.all())
        title = li.name
    print_type = request.GET.get('type', '1')
    return render(request, 'list_words.html', {'list_words': word_list, 'title': title, 'type': print_type})


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
