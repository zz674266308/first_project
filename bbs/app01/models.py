#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Bbs(models.Model):
    category = models.ForeignKey('Category')
    title = models.CharField('标题',max_length=64)
    summary = models.CharField('摘要',max_length=256,null=True,blank=True)
    content = models.TextField('内容')
    author = models.ForeignKey('Bbs_user')
    view_count = models.IntegerField('浏览数',null=True,blank=True)
    ranking = models.IntegerField('排名',null=True,blank=True)
    creation_time = models.DateTimeField('添加时间',auto_now_add=True)
    update_time = models.DateTimeField('更新时间',auto_now=True)

    def __unicode__(self):
        return self.title


class Category(models.Model):
    name = models.CharField('类型',max_length=32,unique=True)

    def __unicode__(self):
        return self.name


class Bbs_user(models.Model):
    CHOICE = (('男','男'),('女','女'))
    user = models.OneToOneField(User,unique=True,related_name='bbs')
    gender = models.CharField('性别',max_length=8,choices=CHOICE,null=True,blank=True)
    name = models.CharField('姓名',max_length=32,default='暂时不知道用什么网名')
    signature = models.CharField('个性签名',max_length=64,default='这个家伙很懒,什么都没有留下...')
    photo = models.ImageField('头像',upload_to='images/',default='images/index.jpeg')

    def __unicode__(self):
        return '%s'%(self.user)


class Comment(models.Model):
    bbs = models.ForeignKey(Bbs)
    author = models.ForeignKey(Bbs_user)
    comment = models.TextField('评论内容',max_length=1024)
    ladder_comment = models.ForeignKey('Comment',related_name='l_comment',null=True,blank=True)
    c_date = models.DateTimeField('评论时间',auto_now_add=True)

    def __unicode__(self):
        return self.comment


