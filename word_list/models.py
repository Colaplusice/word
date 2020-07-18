import json

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from utils import request_translate


class AutoCreatedField(models.DateTimeField):
    """
    A DateTimeField that automatically populates itself at
    object creation.

    By default, sets editable=False, default=datetime.now.

    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('editable', False)
        kwargs.setdefault('default', now)
        super(AutoCreatedField, self).__init__(*args, **kwargs)


class AutoLastModifiedField(AutoCreatedField):
    """
    A DateTimeField that updates itself on each save() of the model.

    By default, sets editable=False and default=datetime.now.

    """

    def pre_save(self, model_instance, add):
        value = now()
        setattr(model_instance, self.attname, value)
        return value


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.

    """
    created = AutoCreatedField(_('created'))
    modified = AutoLastModifiedField(_('modified'))

    # 不能以此类直接建立表
    class Meta:
        abstract = True


class JSONField(models.TextField):
    """ JSON field implementation on top of django textfield """

    def to_dict(self, value):
        """ convert json string to python dictionary """
        return json.loads(value)

    def to_json(self, value):
        """ convert python dictionary to json string """
        return json.dumps(value)

    def from_db_value(self, value, expression, connection):
        """ convert string from db to python dictionary """
        if value is None:
            return value
        return self.to_dict(value)

    def to_python(self, value):
        """ convert model input value to python dictionary """
        if isinstance(value, dict):
            return value
        if value is None:
            return value
        return self.to_dict(value)

    def get_prep_value(self, value):
        """ convert python dictionary to string before writing to db """
        return self.to_json(value)


# def get_translate(content):
#     text = cache.get(content)
#     if not text:
#         text = request_translate(content)
#     #     将扇贝返回值整个cache住
#     cache.set(content, text)
#     if text.get('msg'):
#         try:
#             translation = text['data']['cn_definition']['defn']
#             return translation
#         except:
#             return '无'


class Word(TimeStampedModel):
    content = models.CharField(max_length=32, unique=True, verbose_name='内容')
    translate = models.CharField(max_length=255, verbose_name='翻译', default='释义会自动更新，无需填写')
    data = JSONField(verbose_name='所有数据', default={})

    @property
    def us_sound_mark(self):
        try:
            return self.data['data']['pronunciations']['us']
        except KeyError:
            return 'none'

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        #     释义没更新
        word_data = request_translate(self.content)
        if word_data['msg'] == 'SUCCESS':
            self.data = word_data
            self.translate = word_data['data']['cn_definition']['defn']
        super(Word, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "单词"


class WordList(TimeStampedModel):
    name = models.CharField(verbose_name='单词表名', max_length=255)
    user = models.ForeignKey(User, verbose_name='用户名', on_delete=models.CASCADE)

    @property
    def list_words(self):
        return self.userword_set.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "用户单词List"


class UserWord(TimeStampedModel):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    list = models.ForeignKey(WordList, on_delete=models.CASCADE)

    def __str__(self):
        return self.word.content

    class Meta:
        verbose_name_plural = "用户单词"
