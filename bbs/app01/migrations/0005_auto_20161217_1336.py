# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20161216_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs_user',
            name='photo',
            field=models.ImageField(default=b'/home/lzr/picture/index.jpeg', upload_to=b'images', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
        migrations.AlterField(
            model_name='bbs_user',
            name='signature',
            field=models.CharField(default=b'\xe8\xbf\x99\xe4\xb8\xaa\xe5\xae\xb6\xe4\xbc\x99\xe5\xbe\x88\xe6\x87\x92,\xe4\xbb\x80\xe4\xb9\x88\xe9\x83\xbd\xe6\xb2\xa1\xe6\x9c\x89\xe7\x95\x99\xe4\xb8\x8b...', max_length=64, verbose_name=b'\xe4\xb8\xaa\xe6\x80\xa7\xe7\xad\xbe\xe5\x90\x8d'),
        ),
    ]
