"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from  extra_apps import xadmin
from django.views.static import serve
from untitled2 import settings
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls,),
    url(r'^xadmin/', xadmin.site.urls,name='xadmin'),
    url(r'',include('ynm.urls')),#用include 来解决链接分组问题
    url(r'^position/', include('position.urls')),  # 用include 来解决链接分组问题
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),#上传文件url地址的设置
    url(r'^captcha', include('captcha.urls')), #注册页面提供图片验证码的第三方包的url
]
