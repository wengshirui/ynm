__author__ = 'wsr'
__date__ = '2018/11/9 0009 下午 4:25'

'''工作岗位的业务处理文件'''
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^list/$', PositionListView.as_view(),name='position_list'), #登录页面链接
]