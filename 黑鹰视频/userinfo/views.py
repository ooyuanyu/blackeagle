from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.contrib.auth import logout

import logging


# Create your views here.

# def index(request):
#     return render(request, 'index.html')
def Banner_(request):
    banner1 = Banner.objects.filter(index='1')
    print(banner1)
    banner2 = Banner.objects.filter(index='2')
    banner3 = Banner.objects.filter(index='3')
    banner4 = Banner.objects.filter(index='4')
    banner5 = Banner.objects.filter(index='5')
    banner6 = Banner.objects.filter(index='6')
    banner7 = Banner.objects.filter(index='7')
    # videoinfo = VideoInfo.objects.filter(is_banner=False)[:7]
    return render(request, 'index.html', locals())


def login_(request):
    return render(request, 'login.html')


def loginin(request):
    if request.method == 'POST':
        user = UserInfo()
        user.user = request.POST.get('username')
        user.password = request.POST.get('pwd')
        try:
            find_user = UserInfo.objects.filter(username=user.user)
            if len(find_user) <= 0:
                return render(request, 'login.html', {'message': '用户未注册'})
            if user.password != find_user[0].userpassword:
                return render(request, 'login.html', {'message': '用户名密码错误'})
            if not user.isactive:
                return render(request, 'login.html', {'message': '用户未被激活'})
        except ObjectDoesNotExist as e:
            logging.warning(e)
        request.session['user_name'] = find_user[0].username
        return render(request, 'index.html', {'welcome': '欢迎'})
    return render(request, 'index.html')


def registerin(request):
    if request.method == 'POST':
        new_user = UserInfo()
        new_user.username = request.POST.get('username')
        if " " in new_user.username:
            return HttpResponseRedirect('/userinfo/login/?message2=用户名不能有空格#toregister')
        try:
            olduser = UserInfo.objects.filter(username=new_user.username)
            if len(olduser) > 0:
                return HttpResponseRedirect("/userinfo/login/?message2=用户名重复#toregister")
        except ObjectDoesNotExist as e:
            logging.warning(e)
        if request.POST.get('upwd') != request.POST.get('cpwd'):
            return HttpResponseRedirect("/userinfo/login/?message3=两次密码不一致,请重新输入#toregister")
        new_user.userpassword = request.POST.get('upwd')
        try:
            new_user.save()
        except ObjectDoesNotExist as e:
            logging.warning(e)
        return render(request, 'login.html')


def Logout(request):
    # del request.session['user_name']
    # return HttpResponseRedirect('/')
    logout(request)
    from django.urls import reverse
    return HttpResponseRedirect(reverse('index'))


