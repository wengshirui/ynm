from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    '''可以登录平台的用户，比如劳务公司人员、平台人员等'''
    nick_name = models.CharField(verbose_name='昵称',max_length=100)
    img = models.ImageField(verbose_name='用户头像',max_length=200,upload_to='img/%Y/%m',default='img/default1.jpg')

    def __str__(self):
        return  self.username

    class Meta:
        verbose_name = '登录用户'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    '''管理首页的banner图片等推荐位，前端与推荐位通过id关联'''
    name = models.CharField(verbose_name='推荐位名称',max_length=100)
    img = models.ImageField(verbose_name='图片',max_length=200,upload_to='ban_img/%Y/%m',default='img/default1.jpg')
    url = models.URLField(verbose_name='链接',max_length=100,blank=True,null=True)
    desc = models.TextField(verbose_name='备注',null=True,default='',blank=True)
    add_time = models.DateTimeField(verbose_name='添加时间',auto_now_add=True)
    upd_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name