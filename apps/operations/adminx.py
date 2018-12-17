__author__ = 'wsr'
__date__ = '2018/11/21 0021 上午 9:20'

import xadmin
from .models import *


class EnrollAdmin(object):
    '''后台显示工人报名信息'''
    list_display = ['enroll_id', 'worker','company', 'position','add_time','upd_time']
    search_fields = ['enroll_id', 'worker','company', 'position',]
    list_filter = ['enroll_id', 'worker','company', 'position','add_time','upd_time']
    model_icon = 'fa fa-sign-in'
    relfield_style = 'fk_ajax'


class RecruitAdmin(object):
    '''后台显示公司录取信息'''
    list_display = ['recruit_id', 'worker','company', 'position','add_time','upd_time']
    search_fields = ['recruit_id', 'worker','company', 'position',]
    list_filter = ['recruit_id', 'worker','company', 'position','add_time','upd_time']
    model_icon = 'fa fa-gavel'
    relfield_style = 'fk_ajax'


class WorkerJudgeAdmin(object):
    '''后台显示工人评价'''
    list_display = ['judge_id', 'worker','company', 'position','work_envir_score','work_salary_score','work_leader_score','add_time','upd_time']
    search_fields = ['judge_id', 'worker','company', 'position','work_envir_score','work_salary_score','work_leader_score',]
    list_filter = ['judge_id', 'worker','company', 'position','work_envir_score','work_salary_score','work_leader_score','add_time','upd_time']
    model_icon = 'fa fa-hand-o-left'
    relfield_style = 'fk_ajax'


class CompanyJudgeAdmin(object):
    '''后台显示公司评价'''
    list_display = ['judge_id', 'worker','company', 'position','worker_ability_score','worker_ability_content','leader_content','add_time','upd_time']
    search_fields = ['judge_id', 'worker','company', 'position','worker_ability_score','worker_ability_content','leader_content',]
    list_filter = ['judge_id', 'worker','company', 'position','worker_ability_score','worker_ability_content','leader_content','add_time','upd_time']
    model_icon = 'fa fa-hand-o-right'
    relfield_style = 'fk_ajax'


xadmin.site.register(Enroll, EnrollAdmin)
xadmin.site.register(Recruit, RecruitAdmin)
xadmin.site.register(WorkerJudge, WorkerJudgeAdmin)
xadmin.site.register(CompanyJudge, CompanyJudgeAdmin)