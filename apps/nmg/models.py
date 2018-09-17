from django.db import models
import django.utils.timezone as timezone


# Create your models here.  #将一个工人的信息分成五张表，但需要在后台显示在一起，学校，公司，岗位，技能做到选择或填写
class NewWorkerModel(models.Model):
    '''工人的基本信息，与平台用户不一样'''
    worker_name = models.CharField(max_length=30,verbose_name='工人姓名',default='')
    img = models.ImageField(verbose_name='头像',max_length=200,null=True,blank=True,)
    gender = models.CharField(max_length=10,verbose_name='性别',choices=(('female','女'),('male','男')),default='female')
    age = models.IntegerField(verbose_name='年龄',null=True)
    phone = models.CharField(verbose_name='手机号',max_length=11,default='')
    email = models.EmailField(verbose_name='邮箱',null=True,blank=True,)
    work_years = models.IntegerField(verbose_name='工龄',null=True)
    state = models.CharField(verbose_name='在职状态',choices=(('yes','在职'),('no','离职'),('other','在职，寻找机会')),default='no',max_length=20)
    now_salary = models.IntegerField(verbose_name='目前薪资', default='', help_text='每月工资',blank=True,null=True)
    desc = models.TextField(verbose_name='个人简介',null=True,blank=True,default='')
    add_time = models.DateTimeField(verbose_name='添加时间',auto_now_add=True)
    upd_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)
    #更新人,是否为激活状态，可以后期添加

    def __str__(self):
        return self.worker_name

    class Meta:
        verbose_name = '工人信息'
        verbose_name_plural = verbose_name


class WorkerEduModel(models.Model): #工人的教育信息
    worker = models.ForeignKey(NewWorkerModel,on_delete=models.CASCADE,verbose_name='工人')
    school_name = models.CharField(max_length=30,verbose_name='学校名称')
    start_time = models.DateField(verbose_name='开始时间')
    end_time = models.DateField(verbose_name='结束时间')
    degree = models.CharField(max_length=30,verbose_name='学位学历',help_text='如：初中')
    major = models.CharField(max_length=30,verbose_name='专业',null=True,blank=True,)
    add_time = models.DateTimeField(verbose_name='添加时间',auto_now_add=True)
    upd_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)
    #更新人,是否为激活状态，可以后期添加

    def __str__(self):
        return self.school_name

    class Meta:
        verbose_name = '教育经历'
        verbose_name_plural = verbose_name


class WorkerWorkModel(models.Model): #工人的工作经验
    worker = models.ForeignKey(NewWorkerModel,on_delete=models.CASCADE,verbose_name='工人')
    com_name = models.CharField(max_length=30,verbose_name='公司名称')
    start_time = models.DateField(verbose_name='开始时间')
    end_time = models.DateField(verbose_name='结束时间')
    position = models.CharField(max_length=30,verbose_name='岗位')#需要和岗位关联或输入
    skill = models.CharField(max_length=30,verbose_name='技能等级',help_text='一级瓦工',blank=True,)#需和技能关联
    desc = models.TextField(verbose_name='描述',null=True,blank=True,default='')
    add_time = models.DateTimeField(verbose_name='添加时间',auto_now_add=True)
    upd_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)
    #工作经验是否认证，谁认证的

    def __str__(self):
        return self.com_name

    class Meta:
        verbose_name = '工作经验'
        verbose_name_plural = verbose_name


class WorkerProjectModel(models.Model): #工人的工作经验
    worker = models.ForeignKey(NewWorkerModel,on_delete=models.CASCADE,verbose_name='工人')
    pro_name = models.CharField(max_length=30,verbose_name='项目名称')
    start_time = models.DateField(verbose_name='开始时间')
    end_time = models.DateField(verbose_name='结束时间')
    position = models.CharField(max_length=30,verbose_name='岗位')#需要和岗位关联或输入
    skill = models.CharField(max_length=30,verbose_name='技能等级',help_text='一级瓦工',blank=True,)#需和技能关联
    desc = models.TextField(verbose_name='描述',null=True,blank=True,default='')
    add_time = models.DateTimeField(verbose_name='添加时间',auto_now_add=True)
    upd_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)
    #项目成果，何人认证
    def __str__(self):
        return self.pro_name

    class Meta:
        verbose_name = '项目经验'
        verbose_name_plural = verbose_name


class WorkerSkilltModel(models.Model): #工人的技能,技能和岗位需要另外的表
    worker = models.ForeignKey(NewWorkerModel,on_delete=models.CASCADE,verbose_name='工人')
    skill_name = models.CharField(max_length=30,verbose_name='技能名称',default='')
    grade = models.IntegerField(verbose_name='技能等级',default=1)
    add_time = models.DateTimeField(verbose_name='添加时间',auto_now_add=True)
    upd_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)
    #技能认证人
    def __str__(self):
        return self.skill_name

    class Meta:
        verbose_name = '工人技能'
        verbose_name_plural = verbose_name
