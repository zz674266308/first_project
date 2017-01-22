# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0015_remove_category_administrator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bbs',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
