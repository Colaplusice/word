# Generated by Django 2.2.10 on 2020-07-18 03:31

from django.db import migrations
import word_list.models


class Migration(migrations.Migration):

    dependencies = [
        ('word_list', '0009_auto_20200718_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='data',
            field=word_list.models.JSONField(default={}, verbose_name='所有数据'),
        ),
    ]