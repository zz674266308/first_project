# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bbs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('summary', models.CharField(max_length=256, null=True, verbose_name=b'\xe6\x91\x98\xe8\xa6\x81', blank=True)),
                ('content', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('view_count', models.IntegerField(verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe6\x95\xb0')),
                ('ranking', models.IntegerField(verbose_name=b'\xe6\x8e\x92\xe5\x90\x8d')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='Bbs_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('signature', models.CharField(default=b'\xe8\xbf\x99\xe4\xb8\xaa\xe4\xba\xba\xe5\xbe\x88\xe6\x87\x92\xef\xbc\x8c\xe4\xbb\x80\xe4\xb9\x88\xe9\x83\xbd\xe6\xb2\xa1\xe6\x9c\x89\xe7\x95\x99\xe4\xb8\x8b...', max_length=64, verbose_name=b'\xe4\xb8\xaa\xe6\x80\xa7\xe7\xad\xbe\xe5\x90\x8d')),
                ('photo', models.ImageField(default=b'http://www.sucaijishi.com/uploadfile/2014/0524/20140524012042568.jpg', upload_to=b'photo/', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('administrator', models.ForeignKey(to='app01.Bbs_user')),
            ],
        ),
        migrations.AddField(
            model_name='bbs',
            name='author',
            field=models.ForeignKey(to='app01.Bbs_user'),
        ),
    ]
