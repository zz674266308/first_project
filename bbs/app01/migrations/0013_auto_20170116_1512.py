# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0012_auto_20170116_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs_user',
            name='gender',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'\xe7\x94\xb7', b'\xe7\x94\xb7'), (b'\xe5\xa5\xb3', b'\xe5\xa5\xb3')]),
        ),
    ]
