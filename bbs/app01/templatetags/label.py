#encoding:utf-8
import sys
sys.path.append("..")
from django import template
import uuid
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

register = template.Library()
@register.simple_tag
def Comment_tree(ladder,judge,user):
    if judge:
        s_tr = '<input type="submit" value="发表" />'
    else:
        s_tr = '<input type="button" onclick="duihua()" value="发表" />'
    s = "<div>"
    n = 20
    floor = 1
    if ladder != {}:
        item = ladder.items()
        ite = sorted(item,key=lambda x:x[0].c_date)
        for i,j in ite:
            floor += 1
            if user == i.author.user:
                div = '''<li style="float:left;width:900px;font-size:12px;color:#550">{}</li>
                         <li style="float:left;width:40px;"><a href="javascript:if(confirm('确实要删除该内容吗?'))location='/delete/{}'" style="color:F8F8F8">删除</a></li>'''.format(i.c_date,i.id)
            else:
                div = '<li style="float:left;width:940px;font-size:12px;color:#550">{}</li>'.format(i.c_date)

            s1 = '''<div class="hello" style="margin-left:{n}px">
                        <ul>
                            <div style="padding-bottom:2px;padding-left:2px;color:pink;border-bottom:ridge;
                            border-left:ridge;width:980px;height:auto">
                                <li style="float:left;font-size:20px;color:#174">{}</li>
                                <li style="font-size:20px;color:#501">楼</li>
                                <a href="#" style="font-size:16px;color:blue">{}</a>
                                <div style="width:980px;font-size:14px;color:#333">{}</div>
                                {div}
                                <li><a href="###" style="color:pink" onclick="openShutManager(this,'{m}',false,'取消','回复')">回复</a></li>
                            </div>
                            <div id="{m}" style="margin-right:20px;display:none">
                                <p></p>
                                <div>
                                    <form action="/comments/" method="post">
                                    <textarea style="font-size:14px" name="comment"></textarea>
                                    <input type="hidden" name="id" value="{}" />
                                    <input type="hidden" name="floor" value="other" />
                                    {u}
                                    </form>
                                </div>
                                <p style="height:2px">&nbsp;</p>
                                <div style="BORDER-TOP: pink 1px dashed; OVERFLOW: hidden; HEIGHT: 1px;width:980px">
                            </div>
                        </ul>
                    </div>
                    '''.format(floor,i.author.name,i.comment,i.id,n=n,m=uuid.uuid1(),u=s_tr,div=div)
            s += s1
            if j != {}:
                s = Split(n+40,j,s,judge,user)
            else:
                continue
    else:
        return None
    return s + '</div>'

def Split(n,x,y,judge,user):
    if judge:
        s_tr = '<input type="submit" value="发表" />'
    else:
        s_tr = '<input type="button" onclick="duihua()" value="发表" />'
    item = x.items()
    ite = sorted(item,key=lambda x:x[0].c_date)
    for i,j in ite:
        if user == i.author.user:
            div = '''<li style="float:left;width:{}px;font-size:12px;color:#550">{}</li>
                     <li style="float:left;width:40px;"><a href="javascript:if(confirm('确实要删除该内容吗?'))location='/delete/{}'" style="color:F8F8F8">删除</a></li>'''.format(920-n,i.c_date,i.id)

        else:
            div = '<li style="float:left;width:{}px;font-size:12px;color:#550">{}</li>'.format(960-n,i.c_date)

        s1 = '''<div class="hello" style="margin-left:{}px">
                    <ul>
                        <div style="padding-bottom:2px;padding-left:2px;color:pink;border-bottom:ridge;border-left:ridge;
                        width:{p}px;height:auto">
                            <a href="#" style="font-size:16px;color:blue">{}</a>
                            <div style="width:{p}px;font-size:14px;color:#333">{}</div>
                            {div}
                            <li><a href="###"  style="color:pink" onclick="openShutManager(this,'{m}',false,'取消','回复')">回复</a></li>
                        </div>
                        <div id="{m}" style="margin-right:20px;display:none">
                            <p></p>
                            <div>
                                <form action="/comments/" method="post">
                                    <textarea style="font-size:14px" name="comment"></textarea>
                                    <input type="hidden" name="id" value="{}" />
                                    <input type="hidden" name="floor" value="other" />
                                    {u}
                                </form>
                            </div>
                            <p style="height:2px">&nbsp;</p>
                            <div style="BORDER-TOP: red 1px dashed; OVERFLOW: hidden; HEIGHT: 1px;width:{p}px">
                        </div>
                    </ul>
                </div>
                    '''.format(n,i.author.name,i.comment,i.id,m=uuid.uuid1(),p=1000-n,u=s_tr,div=div)
        y += s1
        if j != {}:
            y = Split(n+40,j,y,judge,user)
    return y



@register.simple_tag
def Add(bbs,user):
    if user == bbs.author.user:
        add_to = '''<li style="float:left;width:926px;font-size:12px;color:#550">{}</li>
                    <li style="float:left;width:40px;"><a href="javascript:if(confirm('确实要删除该内容吗?'))location='/delete_bbs/{}'" style="color:F8F8F8">删除</a></li>'''.format(bbs.creation_time,bbs.id)
    else:
        add_to = '<li style="float:left;width:966px;font-size:12px;color:#550">{}</li>'.format(bbs.creation_time)
    return add_to


@register.simple_tag
def Judge(judge):
    if judge:
        s_tr = '<input type="submit" value="发表" />'
    else:
        s_tr = '<input type="button" onclick="duihua()" value="发表" />'
    return s_tr


@register.simple_tag
def Choice(gender):
    if gender == '男':
        result = '''<p><input name='sex' checked="checked" type='radio' value='男' />男<input name='sex' type='radio' value='女' />女</p>'''
    elif gender == '女':
        result = '''<p><input name='sex' type='radio' value='男' />男<input name='sex' type='radio' checked="checked" value='女' />女</p>'''
    else:
        result = '''<p><input name='sex' type='radio' value='男' />男<input name='sex' type='radio' value='女' />女</p>'''
    return result



@register.simple_tag(takes_context=True)
def Paginate(context, object_list, page_count):
    content = Paginator(object_list,page_count)
    pages = content.num_pages
    try:
        num = context['request'].GET.get('page')
        context['current_page'] = content.page(num)
        l = Left(context['current_page'],content)+Right(context['current_page'],content)
    except PageNotAnInteger:
        num = 1
        if pages <= 3:
            l = [i for i in range(1,pages+1)]
        else:
            l = [1,2,3]
        context['current_page'] = content.page(num)
    l = list(set(l))
    l.sort()
    context['l'] = l
    context['antepenultimate'] = pages-3
    context['content'] = content
    context['pages'] = pages
    return ''


def Left(a,b):
    if a.number == 1:
        l = []
    else:
        try:
            l = [i for i in range(b.page(a.number-2).number,a.number+1)]
        except EmptyPage:
            l = [i for i in range(1,a.number+1)]
    return l


def Right(a,b):
    try:
        l = [i for i in range(a.number,b.page(a.number+2).number+1)]
    except EmptyPage:
        l = [i for i in range(a.number,b.num_pages+1)]
    return l
