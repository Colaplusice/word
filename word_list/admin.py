# Register your models here.

from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.db.models import ManyToOneRel, ForeignKey, OneToOneField, ManyToManyRel

from word_list.models import WordList, Word


class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        self.list_select_related = [x.name for x in model._meta.fields if isinstance(x, (ManyToOneRel, ForeignKey, OneToOneField, ManyToManyRel))]

        # self.search_fields=[model.p]
        super(ListAdminMixin, self).__init__(model, admin_site)


# class Admin(admin.ModelAdmin):
#     pass
class WordAdmin(admin.ModelAdmin):
    autocomplete_fields = ('list',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(WordAdmin, self).get_form(request, obj, **kwargs)
        log = LogEntry.objects.filter(content_type__model='word').order_by('-action_time').first()
        word = log.get_edited_object()
        list = word.list.first()
        form.base_fields['list'].initial = list
        return form
    # prepopulated_fields = {'list': ('list',)}
    # def save_model(self, request, obj, form, change):
    #     obj.list = WordList.objects.first()
    #
    # def save_formset(self, request, form, formset, change):
    #     instances = formset.save(commit=False)
    #     instances.list = WordList.objects.first()
    #     instances.save()
    #     formset.save()


class ListAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    # ordering = ['date_created']

    # print session
    # def _session_data(self, obj):
    #     return pprint.pformat(obj.get_decoded()).replace('\n', '<br>\n')
    #
    # _session_data.allow_tags = True
    # list_display = ['session_key', '_session_data', 'expire_date']
    # readonly_fields = ['_session_data']
    # exclude = ['session_data']

    # date_hierarchy = 'expire_date'
    #
    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #
    #     # 找出最近操作的单词
    #     log = LogEntry.objects.all().order_by('-action_time').first()
    #     word = log.get_edited_object()
    #     list = word.list.all()
    #     kwargs['queryset'] = list
    #     super().formfield_for_manytomany(db_field, request, **kwargs)


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
admin.site.register(WordList, ListAdmin)
