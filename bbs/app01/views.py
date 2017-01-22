#encoding:utf-8
from django.shortcuts import render,HttpResponseRedirect,render_to_response
from django.http import HttpResponse
from models import Bbs, Comment, Bbs_user, Category
from forms import Login_form,Register_form
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone
import os
import time
from bbs.settings import MEDIA_ROOT
# Create your views here.


def Culture(request):
    bbs = Bbs.objects.all()
    category = Category.objects.all().order_by('id')
    user = request.user
    if user.is_superuser:
        auth.logout(request)
        return render(request, '2.html', {'bbs':bbs,'judge':False,'category':category})
    elif user.is_authenticated():
        bbs_user = Bbs_user.objects.get(user_id=user.id)
        images = '../static/media/'+str(bbs_user.photo)
        return render(request, '2.html', {'bbs':bbs,'user':user,'bbs_user':bbs_user,
                                          'images':images,'judge':True,'category':category})
    else:
        return render(request, '2.html', {'bbs':bbs,'judge':False,'category':category})


def Section(request,sec_id):
    bbs = Bbs.objects.filter(category__id=sec_id)
    category = Category.objects.all().order_by('id')
    user = request.user
    if user.is_superuser:
        auth.logout(request)
        return render(request, '2.html', {'bbs':bbs,'judge':False,'category':category,'sec_id':int(sec_id)})
    elif user.is_authenticated():
        bbs_user = Bbs_user.objects.get(user_id=user.id)
        images = '../static/media/'+str(bbs_user.photo)
        return render(request, '2.html', {'bbs':bbs,'user':user,'bbs_user':bbs_user,
                                          'images':images,'judge':True,'category':category,'sec_id':int(sec_id)})
    else:
        return render(request, '2.html', {'bbs':bbs,'judge':False,'category':category,'sec_id':int(sec_id)})


def Hello(request,pk):
    bbs = Bbs.objects.get(pk=pk)
    category = Category.objects.all().order_by('id')
    comment = bbs.comment_set.all().order_by('c_date')
    dic = {}
    ladder = Ladder(comment,dic)
    count = len(comment)
    user = request.user
    if user.is_superuser:
        auth.logout(request)
        return render(request, '1.html',
                  {'bbs':bbs, 'comment':comment, 'count':count, 'ladder':ladder,
                   'judge':False,'user':None,'category':category

                   }
                  )
    elif user.is_authenticated():
        bbs_user = Bbs_user.objects.get(user_id=user.id)
        images = '../static/media/'+str(bbs_user.photo)
        return render(request, '1.html',
                  {'bbs':bbs, 'comment':comment, 'count':count, 'ladder':ladder,
                    'user':user,'bbs_user':bbs_user,'images':images,'judge':True,
                    'category':category
                   }
                  )
    else:
        return render(request, '1.html',
                  {'bbs':bbs, 'comment':comment, 'count':count, 'ladder':ladder,
                    'judge':False,'user':None,'category':category
                   }
                  )


def Ladder(comment,dic):
    if dic == {}:
        for i in comment:
            if i.ladder_comment == None:
                dic[i] = {}

    for i in comment:
        for j,k in dic.items():
            if i.ladder_comment == j:
                k[i] = {}
                Ladder(comment,k)
            else:
                continue
    return dic


def Login(request):
    if request.method == 'POST':
        form = Login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        result = auth.authenticate(username=username,password=password)
        if result is not None:
            if result.is_active:
                auth.login(request,result)
                return HttpResponseRedirect('/culture')

        else:
            return HttpResponse('帐号或密码错误')
    return render(request,'login.html')


def Logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/culture')


def Register(request):
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            result = User.objects.filter(username=username)
            if len(result) > 0:
                return HttpResponse('该用户已经存在，请重新输入！')
            else:
                if password1 != password2:
                    return HttpResponse('两次密码不一致，请重新输入！')
                else:
                    user = User.objects.create_user(username=username,password=password1)
                    user.save()
                    bbs_user = Bbs_user.objects.create(user=user)
                    bbs_user.save()
                    return HttpResponse('恭喜您，注册成功！')
    return render(request,'register.html')


def Publish(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('title')
            summary = request.POST.get('summary')
            content = request.POST.get('content')
            name = request.POST.get('state','')
            print name
            print type(name)
            category = Category.objects.get(name=name)
            author = Bbs_user.objects.get(user=request.user)
            if content[:3] == '<p>' and content[-4:] == '</p>':
                    content = content[3:-4]
            s = str(content).replace(' ','')
            s2 = s.replace('&nbsp;','')
            if len(s2)>0:
                Bbs.objects.create(category=category,title=title,summary=summary,content=content,
                                    author=author)
                return HttpResponseRedirect('/culture')
            else:
                return HttpResponse('内容不能为空！')


def Comments(request):
    user = request.user
    if user.is_authenticated():
        if request.method == 'POST':
            comment = request.POST.get('comment')
            id = request.POST.get('id','')
            floor = request.POST.get('floor')
            if floor == 'first':
                parent=None
                bbs = Bbs.objects.get(id=id)
            else:
                parent = Comment.objects.get(id=id)
                bbs = parent.bbs
            if comment[:3] == '<p>' and comment[-4:] == '</p>':
                    comment = comment[3:-4]
            s = str(comment).replace(' ','')
            s2 = s.replace('&nbsp;','')
            if len(s2)>0:
                bbs_user = Bbs_user.objects.get(user=user)
                Comment.objects.create(bbs=bbs,author=bbs_user,
                                        comment=comment,ladder_comment=parent,
                                        c_date=timezone.now())
                return HttpResponseRedirect('/hello/%s'%bbs.pk)
            else:
                return HttpResponse('内容不能为空！')


def Delete_bbs(request,id):
    result = Bbs.objects.get(id=id)
    result.delete()
    return HttpResponseRedirect('/culture')


def Delete(request,id):
    result = Comment.objects.get(id=id)
    num = result.bbs.pk
    result.delete()
    return HttpResponseRedirect('/hello/%s'%num)


def Personal(request):
    user = request.user
    bbs_user = Bbs_user.objects.get(user=user)
    bbs = Bbs.objects.filter(author=bbs_user)
    images = '../static/media/'+str(bbs_user.photo)
    return render(request,'personal.html',{'bbs_user':bbs_user,'bbs':bbs,'images':images})


def Data(request):
    user=request.user
    bbs_user = Bbs_user.objects.get(user=user)
    gender = bbs_user.gender
    images = '../static/media/%s'%str(bbs_user.photo)
    return render(request,'data.html',{'bbs_user':bbs_user,'gender':gender,'images':images})


def Modify(request):
    if request.method == 'POST':
        name = request.POST.get('fullname','')
        gender = request.POST.get('sex','')
        signature = request.POST.get('signature','')
        try:
            photo = request.FILES['images']
            p,q = os.path.splitext(photo.name)
            str1 = time.strftime('%y%m%d%H%M%S')
            str2 = '%s%s'%(str1,q)
            file_name = os.path.join(MEDIA_ROOT,'images',str2)
            new_name = 'images/%s'%str2
            with open(file_name,'w') as f:
                for i in photo.chunks(10240):
                    f.write(i)
            bbs_user = Bbs_user.objects.filter(user=request.user)
            bbs_user.update(name=name,gender=gender,signature=signature,photo=new_name)

        except:
            bbs_user = Bbs_user.objects.filter(user=request.user)
            bbs_user.update(name=name,gender=gender,signature=signature)

        return HttpResponseRedirect('/data')

'''
def Ldd():
    bbs = Bbs.objects.get(pk=1)
    comment = bbs.comment_set.all()
    dic = {}
    if dic == {}:
        for i in comment:
            if i.ladder_comment == None:
                dic[i] = {}

    for i in comment:
        for j,k in dic.items():
            if i.ladder_comment == j:
                k[i] = {}
                Ladder(k,dic)




def Ladder(x,y):
    bbs = Bbs.objects.get(pk=1)
    comment = bbs.comment_set.all()
    for i in comment:
        for j,k in x.items():
            if i.ladder_comment == j:
                k[i] = {}
                Ladder(k,y)
            else:
                continue
    return y

'''















