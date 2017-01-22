# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs_user',
            name='gender',
            field=models.CharField(default=1, max_length=1, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(0, b'\xe7\x94\xb7'), (1, b'\xe5\xa5\xb3')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bbs_user',
            name='name',
            field=models.CharField(default=1, max_length=32, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d'),
            preserve_default=False,
        ),
    ]
