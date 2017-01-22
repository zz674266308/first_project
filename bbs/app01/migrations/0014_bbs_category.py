# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0013_auto_20170116_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs',
            name='category',
            field=models.ForeignKey(default=1, to='app01.Category'),
            preserve_default=False,
        ),
    ]
