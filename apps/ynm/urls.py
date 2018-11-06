__author__ = 'wsr'
__date__ = '2018/10/25 0025 下午 4:08'

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index,name='index'), #首页链接
    url(r'^login/$', LoginView.as_view(),name='login'), #登录页面链接
    url(r'^register/$', RegisterView.as_view(), name='register'), #注册页面链接
]