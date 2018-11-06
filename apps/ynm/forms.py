__author__ = 'wsr'
__date__ = '2018/10/22 0022 下午 2:00'
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    '''登录表单验证，在数据库验证之前的操作'''
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={'invalid':'验证码错误',})