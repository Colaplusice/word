from django.http import HttpResponse
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


def export_list(request, list_id):
    word_list = WordList.objects.get(id=list_id)
    # content = ''
    file_name = '{}.txt'.format(word_list.name)
    # with open(file_name, 'w')as opener:
    content = '\n'.join([word.word.content for word in word_list.list_words])
    print(content)
    #     for word in word_list.list_words:
    #         opener.write(word.word.content + '\n')
    response = HttpResponse(content, content_type='application/text charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)

    # res = FileResponse(io.StringIO(content).read(), filename=file_name, as_attachment=True)
    # res['Content-Type'] = 'application/octet-stream'
    return response


def get_translate():
    pass
