from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class TradeModel(models.Model):
    '''行业 如旅游 电子商务  零售等，'''
    name = models.CharField(verbose_name='行业名称',max_length=100)
    desc = models.TextField(verbose_name='行业描述',null=True,default='')
    example = models.CharField(verbose_name='著名公司',max_length=200,blank=True)
    add_time = models.DateTimeField(verbose_name='添加时间',default=timezone.now)
    upd_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '行业信息'
        verbose_name_plural = verbose_name


class PositionModel(models.Model):
    '''岗位，如产品经理，木工，水电工等'''
    name = models.CharField(verbose_name='岗位名称',max_length=100)
    desc = models.TextField(verbose_name='岗位描述',null=True,default='')
    skill = models.CharField(max_length=30,verbose_name='所需技能',help_text='一级瓦工',blank=True,)#需和技能关联
    add_time = models.DateTimeField(verbose_name='添加时间',default=timezone.now)
    upd_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '岗位信息'
        verbose_name_plural = verbose_name


class SkillModel(models.Model):
    '''技能信息，如瓦工一级，水电工一级'''
    name = models.CharField(verbose_name='技能名称',max_length=100)
    grade = models.IntegerField(verbose_name='技能等级',default=0)
    desc = models.TextField(verbose_name='岗位描述',default='')
    add_time = models.DateTimeField(verbose_name='添加时间',default=timezone.now)
    upd_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '技能信息'
        verbose_name_plural = verbose_name