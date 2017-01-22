# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20161220_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(max_length=1024, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('c_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('author', models.ForeignKey(to='app01.Bbs_user')),
                ('bbs', models.ForeignKey(to='app01.Bbs')),
                ('ladder_comment', models.ForeignKey(related_name='l_comment', blank=True, to='app01.Comment', null=True)),
            ],
        ),
    ]
