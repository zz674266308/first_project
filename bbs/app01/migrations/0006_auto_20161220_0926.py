# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20161217_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs_user',
            name='photo',
            field=models.ImageField(default=b'images/index.jpeg', upload_to=b'images/', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
    ]
