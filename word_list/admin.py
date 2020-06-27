# Register your models here.

from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import ManyToOneRel, ForeignKey, OneToOneField, ManyToManyRel

from word_list.models import WordList, Word, UserWord


class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        self.list_select_related = [x.name for x in model._meta.fields if isinstance(x, (ManyToOneRel, ForeignKey, OneToOneField, ManyToManyRel))]

        # self.search_fields=[model.p]
        super(ListAdminMixin, self).__init__(model, admin_site)


# class MyAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Word._meta.get_fields()]


class Admin(ListAdminMixin, admin.ModelAdmin):
    pass


class WordAdmin(Admin):
    search_fields = ('content', 'translate',)

    # 自动补全列表为上一次的
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(WordAdmin, self).get_form(request, obj, **kwargs)
    #     log = LogEntry.objects.filter(content_type__model='word').order_by('-action_time').first()
    #     try:
    #         word = log.get_edited_object()
    #         list = word.list.first()
    #         form.base_fields['list'].initial = list
    #     except ObjectDoesNotExist:
    #         pass
    #     return form

    # prepopulated_fields = {'list': ('list',)}
    # def save_model(self, request, obj, form, change):
    #     obj.list = WordList.objects.first()
    #
    # def save_formset(self, request, form, formset, change):
    #     instances = formset.save(commit=False)
    #     instances.list = WordList.objects.first()
    #     instances.save()
    #     formset.save()


class UserWordAdmin(Admin):
    # list_display = ('word', 'list',)
    autocomplete_fields = ('list', 'word',)

    # ordering = ['date_created']

    # print session
    # def _session_data(self, obj):
    #     return pprint.pformat(obj.get_decoded()).replace('\n', '<br>\n')
    #
    # _session_data.allow_tags = True
    # list_display = ['session_key', '_session_data', 'expire_date']
    # readonly_fields = ['_session_data']
    # exclude = ['session_data']
    def get_form(self, request, obj=None, **kwargs):
        form = super(UserWordAdmin, self).get_form(request, obj, **kwargs)
        log = LogEntry.objects.filter(content_type__model='userword').order_by('-action_time').first()
        try:
            user_word = log.get_edited_object()
            form.base_fields['list'].initial = user_word.list
        except ObjectDoesNotExist:
            pass
        return form

# class UserWordInline(admin.TabularInline):
#     model = UserWord


class UserWordListAdmin(admin.ModelAdmin):
    search_fields = ('name',)

    # inlines = [UserWordInline]
    def all_words(self, obj):
        return '/'.join([str(word) for word in obj.userword_set.all()])

    list_display = [field.name for field in WordList._meta.fields] + ['all_words']

    # list_display = [field.name for field in WordList._meta.get_fields()]

    def get_queryset(self, request):
        qs = super(UserWordListAdmin, self).get_queryset(request)
        return qs.filter(user=request.user)



# models = apps.get_models()
# for model in models:
#     # word单独注册
#     if model._meta.model_name == 'word':
#         admin_class = WordAdmin
#     else:
#         admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
#     try:
#         admin.site.register(model, admin_class)
#     except admin.sites.AlreadyRegistered:
#         pass

admin.site.register(Word, WordAdmin)
admin.site.register(WordList, UserWordListAdmin)
admin.site.register(UserWord, UserWordAdmin)
