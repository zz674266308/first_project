# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_auto_20170115_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='ranking',
            field=models.IntegerField(null=True, verbose_name=b'\xe6\x8e\x92\xe5\x90\x8d', blank=True),
        ),
        migrations.AlterField(
            model_name='bbs',
            name='view_count',
            field=models.IntegerField(null=True, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe6\x95\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='bbs_user',
            name='gender',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'0', b'\xe7\x94\xb7'), (b'1', b'\xe5\xa5\xb3')]),
        ),
    ]
