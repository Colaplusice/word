# Generated by Django 2.2.10 on 2020-07-19 07:26

from django.db import migrations
import word_list.models


class Migration(migrations.Migration):

    dependencies = [
        ('word_list', '0011_auto_20200719_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='data',
            field=word_list.models.JSONField(default='Null', null=True, verbose_name='所有数据'),
        ),
    ]
