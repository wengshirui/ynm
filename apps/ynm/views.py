from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password #密码加密所用
from django.contrib.auth.backends import ModelBackend #登录时候用手机号、昵称、邮箱等
from django.db.models import Q  #解决搜索数据库或的问题
from .models import *
from django.views.generic.base import View
from .forms import *


# Create your views here.
# 这里是处理业务逻辑的地方，比如y=3x，这里写的就是这样的逻辑
class CustomBackends(ModelBackend):
    '''定义登录时候使用昵称或邮箱或手机号等登录字段'''
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def index(request):
    '''处理首页的html，也可以在url中引用from django.views.generic import TemplateView'''
    return render(request,'index.html')


class LoginView(View):
    '''用类的方式，编辑登录逻辑'''
    def post(self,request):#post方式访问页面
        login_form = LoginForm(request.POST) #先用form表单验证下前端数据
        if login_form.is_valid(): #如果通过表单验证
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {})
            else:
                return render(request, 'login.html', {'msg': '用户名密码错误',})
        else:
            return render(request, 'login.html', { 'login_form':login_form}) #数据库判断前先form判断

    def get(self,request): #get方式访问页面
        return render(request, 'login.html', {})

'''def user_login(request):
    #用函数的方式编辑登录逻辑
    if request.method == 'POST':
        user_name = request.POST.get('username','')
        pass_word = request.POST.get('password','')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request,user)
            return render(request,'index.html',{})
        else:
            return render(request,'login.html',{'msg':'用户名密码错误',})
    elif request.method == 'GET':
        return render(request,'login.html',{})
'''


class RegisterView(View):
    '''这个类是用来处理注册业务逻辑的，
    内心无法宁静的时候除了随心所欲之外可以试着坚持去做些自己觉得正确又不想做的事情，也许感受会更好'''

    def get(self,request):
        register_form = RegisterForm()#页面加载时，显示验证码，此处代码是否可简化？
        return render(request,'register.html',{'register_form':register_form,})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email','')
            pass_word = request.POST.get('password','')
            user = UserProfile.objects.get(email=user_name)
            if user is not None:
                return render(request,'register.html',{'msg':'用户已存在'})
            else:
                new_user = UserProfile()
                new_user.username = user_name
                new_user.nick_name = user_name
                new_user.email = user_name
                new_user.password = make_password(pass_word)#讲用户输入的明文密码hash加密储存，这是基本的要求
                new_user.save()
                return render(request,'login.html',)
        else:
            return render(request,'register.html',{'register_form':register_form,})
