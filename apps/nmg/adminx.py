import xadmin
from .models import NewWorkerModel,WorkerEduModel,WorkerWorkModel,WorkerProjectModel,WorkerSkilltModel

#配置后台显示/搜索/过滤字段
class EduInline(object):
    model = WorkerEduModel
    extra = 0

class WorkInline(object):
    model = WorkerWorkModel
    extra = 0


class ProjextInline(object):
    model = WorkerProjectModel
    extra = 0


class SkillInline(object):
    model = WorkerSkilltModel
    extra = 0


class NewWorkerAdmin(object):
    list_display = ['worker_name', 'gender', 'age','work_years','state','add_time','upd_time']
    search_fields = ['worker_name', 'gender', 'age','work_years','state']
    list_filter = ['worker_name', 'gender', 'age','work_years','state','add_time','upd_time']
    ordering = ['work_years']
    relfield_style = 'fk_ajax'
    model_icon = 'fa fa-group'
    inlines = [EduInline,WorkInline,ProjextInline,SkillInline]


class WorkEduAdmin(object):
    list_display = ['worker', 'school_name', 'degree','major','add_time','upd_time']
    search_fields = ['worker', 'school_name', 'degree','major']
    list_filter = ['worker', 'school_name', 'degree','major','add_time','upd_time']
    model_icon = 'fa fa-graduation-cap'


class WorkerWorkAdmin(object):
    list_display = ['worker', 'com_name', 'position','skill','add_time','upd_time']
    search_fields = ['worker', 'com_name', 'position','skill',]
    list_filter = ['worker', 'com_name', 'position','skill','add_time','upd_time']
    model_icon = 'fa fa-gavel'


class WorkerProjectAdmin(object):
    list_display = ['worker', 'pro_name', 'position','skill','add_time','upd_time']
    search_fields = ['worker', 'pro_name', 'position','skill',]
    list_filter = ['worker', 'pro_name', 'position','skill','add_time','upd_time']
    model_icon = 'fa fa-briefcase'


class WorkerSkillAdmin(object):
    list_display = ['worker', 'skill_name', 'grade','add_time','upd_time']
    search_fields = ['worker', 'skill_name', 'grade',]
    list_filter = ['worker', 'skill_name', 'grade','add_time','upd_time']
    model_icon = 'fa fa-handshake-o'


xadmin.site.register(NewWorkerModel, NewWorkerAdmin)
xadmin.site.register(WorkerEduModel, WorkEduAdmin)
xadmin.site.register(WorkerWorkModel, WorkerWorkAdmin)
xadmin.site.register(WorkerProjectModel, WorkerProjectAdmin)
xadmin.site.register(WorkerSkilltModel, WorkerSkillAdmin)
