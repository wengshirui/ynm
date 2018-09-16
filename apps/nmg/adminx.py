import xadmin
from .models import NewWorkerModel,WorkerEduModel,WorkerWorkModel,WorkerProjectModel,WorkerSkilltModel

#配置后台显示/搜索/过滤字段
class NewWorkerAdmin(object):
    list_display = ['worker_name', 'gender', 'age','work_years','add_time','upd_time']
    search_fields = ['worker_name', 'gender', 'age','work_years']
    list_filter = ['worker_name', 'gender', 'age','work_years','add_time','upd_time']


class WorkEduAdmin(object):
    list_display = ['worker', 'school_name', 'degree','major','add_time','upd_time']
    search_fields = ['worker', 'school_name', 'degree','major']
    list_filter = ['worker', 'school_name', 'degree','major','add_time','upd_time']


class WorkerWorkAdmin(object):
    list_display = ['worker', 'com_name', 'position','skill','add_time','upd_time']
    search_fields = ['worker', 'com_name', 'position','skill',]
    list_filter = ['worker', 'com_name', 'position','skill','add_time','upd_time']


class WorkerProjectAdmin(object):
    list_display = ['worker', 'pro_name', 'position','skill','add_time','upd_time']
    search_fields = ['worker', 'pro_name', 'position','skill',]
    list_filter = ['worker', 'pro_name', 'position','skill','add_time','upd_time']


class WorkerSkillAdmin(object):
    list_display = ['worker', 'skill_name', 'grade','add_time','upd_time']
    search_fields = ['worker', 'skill_name', 'grade',]
    list_filter = ['worker', 'skill_name', 'grade','add_time','upd_time']


xadmin.site.register(NewWorkerModel, NewWorkerAdmin)
xadmin.site.register(WorkerEduModel, WorkEduAdmin)
xadmin.site.register(WorkerWorkModel, WorkerWorkAdmin)
xadmin.site.register(WorkerProjectModel, WorkerProjectAdmin)
xadmin.site.register(WorkerSkilltModel, WorkerSkillAdmin)
