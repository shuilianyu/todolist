from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User


#用户注册
class user_register(View):
    def get(self,req):
        return render(req,'user/register.html')
    def post(self,req):
        msg = {
            'username_error':'',
            'password_error1':'',
            'password_error2':'',
        }
        username = req.POST.get('username')
        password1=req.POST.get('password1')
        password2 = req.POST.get('password2')
        if not username:
            msg['username_error']='name is empty'
        elif not password1:
                msg['password_error1']='password is empty'
        elif password1 != password2:
                msg['password_error2']='two password different'
        else:
            #防止数据库中出现用户名相同的情况
            test = User.objects.filter(username = username)
            if len(test)==0:
               #创建user对象
                user = User.objects.create_user(username = username,password=password1)
                user.save()
                return redirect('/user/login/')
            else:
                msg['username_error'] = 'username already exist'
        return render(req,'user/register.html',msg)


class user_login(View):
    def get(self,req):
        return render(req,'user/login.html')
    def post(self,req):
        username = req.POST.get('username')
        password = req.POST.get('password')
        #用户验证,返回用户对象
        user = authenticate(username=username,password=password)
        if user:
            login(req,user=user)
            return redirect('/task/task_list/')
        else:
            return HttpResponse('用户名或者密码错误')


def user_logout(req):
    logout(req)
    return redirect('/')
