from django.db import models
import django.utils.timezone as timezone
from position.models import TradeModel,PositionModel


# Create your models here.
class ComInfoModel(models.Model):
    ''' 公司的基本信息 '''
    name = models.CharField(verbose_name='公司名称',max_length=100,default='')
    trade = models.ForeignKey(TradeModel,verbose_name='所属行业',default='',blank=True,on_delete=models.CASCADE)
    img = models.ImageField(verbose_name='营业执照', max_length=200, null=True, blank=True, upload_to='com_img/%Y/%m')
    address = models.CharField(verbose_name='公司地址',max_length=100,null=True,blank=True,default='')
    credit_no = models.CharField(verbose_name='信用代码',max_length=100,default='',blank=True,)
    desc = models.TextField(verbose_name='公司简介',default='')
    add_time = models.DateTimeField(verbose_name='添加时间',auto_now_add=True)
    upd_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '公司信息'
        verbose_name_plural = verbose_name


class ComContactModel(models.Model):
    '''公司的联系信息，联系人 联系方式  快递地址，一个公司多个联系人信息'''
    company = models.ForeignKey(ComInfoModel,verbose_name='公司',on_delete=models.CASCADE)
    contacts_name = models.CharField(verbose_name='联系人姓名',max_length=100,default='')
    position = models.CharField(max_length=30,verbose_name='岗位',blank=True)#需要和岗位关联或输入
    phone = models.CharField(verbose_name='联系电话',max_length=20,default='')
    address = models.CharField(verbose_name='快递地址',max_length=100,null=True,blank=True,default='')
    add_time = models.DateTimeField(verbose_name='添加时间',auto_now_add=True)
    upd_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    def __str__(self):
        return self.contacts_name

    class Meta:
        verbose_name = '联系信息'
        verbose_name_plural = verbose_name


class ComRecruitModel(models.Model):
    '''公司的招聘信息 岗位 城市 所需技能 描述'''
    company = models.ForeignKey(ComInfoModel,verbose_name='公司',on_delete=models.CASCADE)
    position = models.ForeignKey(PositionModel,verbose_name='岗位',blank=True,on_delete=models.CASCADE)#需要和岗位关联或输入
    city = models.CharField(verbose_name='所在城市',max_length=50)
    skill = models.CharField(max_length=30,verbose_name='技能等级',help_text='一级瓦工',blank=True,default='')#需和技能关联
    desc = models.TextField(verbose_name='岗位描述',null=True,blank=True,default='')
    num = models.IntegerField(verbose_name='招聘人数',default=1)
    min_salary = models.IntegerField(verbose_name='最低薪资',default='',help_text='每月工资')
    max_salary = models.IntegerField(verbose_name='最高薪资',default='',help_text='每月工资')
    add_time = models.DateTimeField(verbose_name='添加时间',auto_now_add=True)
    upd_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = '招聘信息'
        verbose_name_plural = verbose_name