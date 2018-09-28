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