# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20161216_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs_user',
            name='gender',
            field=models.CharField(max_length=8, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'0', b'\xe7\x94\xb7'), (b'1', b'\xe5\xa5\xb3'), (b'2', b'\xe4\xbf\x9d\xe5\xaf\x86')]),
        ),
    ]
