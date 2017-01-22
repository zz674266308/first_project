# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20161222_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs_user',
            name='user',
            field=models.OneToOneField(related_name='bbs', to=settings.AUTH_USER_MODEL),
        ),
    ]
