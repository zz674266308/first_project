# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_auto_20170103_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='ranking',
            field=models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\x90\x8d', blank=True),
        ),
        migrations.AlterField(
            model_name='bbs',
            name='view_count',
            field=models.IntegerField(verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe6\x95\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='bbs_user',
            name='gender',
            field=models.CharField(blank=True, max_length=8, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'0', b'\xe7\x94\xb7'), (b'1', b'\xe5\xa5\xb3'), (b'2', b'\xe4\xbf\x9d\xe5\xaf\x86')]),
        ),
        migrations.AlterField(
            model_name='bbs_user',
            name='name',
            field=models.CharField(default=b'\xe6\x9a\x82\xe6\x97\xb6\xe4\xb8\x8d\xe7\x9f\xa5\xe9\x81\x93\xe7\x94\xa8\xe4\xbb\x80\xe4\xb9\x88\xe7\xbd\x91\xe5\x90\x8d', max_length=32, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d'),
        ),
    ]
