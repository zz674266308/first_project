# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0016_auto_20170117_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b')),
            ],
        ),
        migrations.AddField(
            model_name='bbs',
            name='category',
            field=models.ForeignKey(default=1, to='app01.Category'),
            preserve_default=False,
        ),
    ]
