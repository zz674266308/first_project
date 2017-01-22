# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20161216_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs_user',
            name='gender',
            field=models.CharField(max_length=8, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(0, b'\xe7\x94\xb7'), (1, b'\xe5\xa5\xb3'), (2, b'\xe4\xbf\x9d\xe5\xaf\x86')]),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, max_length=32, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
    ]
