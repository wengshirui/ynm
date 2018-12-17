from django.db import models
from nmg.models import NewWorkerModel
from company.models import ComInfoModel
from position.models import PositionModel

# Create your models here.
#工人报名、公司录取、相互评价等操作；


class Enroll(models.Model):
    '''这里建的表用来记录工人对哪些岗位报名了，'''
    enroll_id = models.IntegerField(verbose_name='报名编号',default=100000)
    worker = models.ForeignKey(NewWorkerModel,verbose_name='工人',on_delete=models.CASCADE)
    company = models.ForeignKey(ComInfoModel,verbose_name='公司',on_delete=models.CASCADE)
    position = models.ForeignKey(PositionModel, verbose_name='岗位', on_delete=models.CASCADE)
    add_time = models.DateTimeField(verbose_name='报名时间',auto_now_add=True)
    upd_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    def __str__(self):
        return  '%s报名了%s%s岗位'%(self.worker,self.company,self.position)

    class Meta:
        verbose_name = '报名信息'
        verbose_name_plural = verbose_name


class Recruit(models.Model):
    '''这里建的表用来记录公司录取了哪些工人，'''
    recruit_id = models.IntegerField(verbose_name='录取编号',default=100000)
    worker = models.ForeignKey(NewWorkerModel,verbose_name='工人',on_delete=models.CASCADE)
    company = models.ForeignKey(ComInfoModel,verbose_name='公司',on_delete=models.CASCADE)
    position = models.ForeignKey(PositionModel, verbose_name='岗位', on_delete=models.CASCADE)
    add_time = models.DateTimeField(verbose_name='录取时间',auto_now_add=True)
    upd_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    def __str__(self):
        return  '%s%s岗位录取了%s'%(self.company,self.position,self.worker)

    class Meta:
        verbose_name = '录取信息'
        verbose_name_plural = verbose_name


class WorkerJudge(models.Model):
    '''这张表是用来记录工人对公司的判断'''
    judge_id = models.IntegerField(verbose_name='评价编号',default=100000)
    worker = models.ForeignKey(NewWorkerModel,verbose_name='工人',on_delete=models.CASCADE)
    company = models.ForeignKey(ComInfoModel,verbose_name='公司',on_delete=models.CASCADE)
    position = models.ForeignKey(PositionModel, verbose_name='岗位', on_delete=models.CASCADE)
    work_envir_score = models.CharField(verbose_name='工作环境评价得分',max_length=10,choices=(('1分','很差'),
                                                                                     ('2分', '较差'),
                                                                                     ('3分', '一般'),
                                                                                     ('4分', '较好'),
                                                                                     ('5分', '很好'),
                                                                                     ),default='4')
    work_envir_content = models.TextField(verbose_name='工作环境评价内容')
    work_envir_img = models.ImageField(verbose_name='工作环境评价图片', max_length=200, null=True, blank=True, upload_to='WorkerJudge/%Y/%m')
    work_salary_score = models.CharField(verbose_name='工作薪资评价得分',max_length=10,choices=(('1分','很差'),
                                                                                     ('2分', '较差'),
                                                                                     ('3分', '一般'),
                                                                                     ('4分', '较好'),
                                                                                     ('5分', '很好'),
                                                                                     ),default='4')
    work_salary_content = models.TextField(verbose_name='工作薪资评价内容')
    work_leader_score = models.CharField(verbose_name='直属领导评价得分',max_length=10,choices=(('1分','很差'),
                                                                                     ('2分', '较差'),
                                                                                     ('3分', '一般'),
                                                                                     ('4分', '较好'),
                                                                                     ('5分', '很好'),
                                                                                     ),default='4')
    work_leader_content = models.TextField(verbose_name='直属领导评价内容')
    add_time = models.DateTimeField(verbose_name='评价时间',auto_now_add=True)
    upd_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    class Meta:
        verbose_name = '工人评价'
        verbose_name_plural = verbose_name


class CompanyJudge(models.Model):
    '''这张表是用来记录工人对公司的判断'''
    judge_id = models.IntegerField(verbose_name='评价编号',default=100000)
    worker = models.ForeignKey(NewWorkerModel,verbose_name='工人',on_delete=models.CASCADE)
    company = models.ForeignKey(ComInfoModel,verbose_name='公司',on_delete=models.CASCADE)
    position = models.ForeignKey(PositionModel, verbose_name='岗位', on_delete=models.CASCADE)
    worker_ability_score = models.CharField(verbose_name='工作能力评价得分',max_length=10,choices=(('1分','很差'),
                                                                                     ('2分', '较差'),
                                                                                     ('3分', '一般'),
                                                                                     ('4分', '较好'),
                                                                                     ('5分', '很好'),
                                                                                     ),default='4')
    worker_ability_content = models.TextField(verbose_name='工作能力评价内容')
    worker_ability_img = models.ImageField(verbose_name='工作能力评价图片', max_length=200, null=True, blank=True, upload_to='CompanyJudge/%Y/%m')
    leader_content = models.TextField(verbose_name='直属领导的批语')
    add_time = models.DateTimeField(verbose_name='评价时间',auto_now_add=True)
    upd_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    class Meta:
        verbose_name = '公司评价'
        verbose_name_plural = verbose_name