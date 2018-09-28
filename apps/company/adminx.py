#author: wengshirui
#datetime: 15/9/18上午8:37

import xadmin
from .models import ComInfoModel,ComContactModel,ComRecruitModel


#配置后台显示/搜索/过滤字段
class ContactInline(object):
    model = ComContactModel
    extra = 0


class RecruitInline(object):
    model = ComRecruitModel
    extra = 0


class ComInfoAdmin(object):
    '''显示公司的基本信息'''
    list_display = ['name', 'trade', 'address','credit_no','add_time','upd_time']
    search_fields = ['name', 'trade', 'address','credit_no',]
    list_filter = ['name', 'trade', 'address','credit_no','add_time','upd_time']
    model_icon = 'fa fa-bank'
    inlines = [ContactInline,RecruitInline]


class ComContactAdmin(object):
    list_display = ['company', 'contacts_name', 'position','phone','add_time','upd_time']
    search_fields = ['company', 'contacts_name', 'position','phone',]
    list_filter = ['company', 'contacts_name', 'position','phone','add_time','upd_time']
    model_icon = 'fa fa-volume-control-phone'


class ComRecruitAdmin(object):
    list_display = ['company', 'position', 'city','num','add_time','upd_time']
    search_fields = ['company', 'position', 'city','num',]
    list_filter = ['company', 'position', 'city','num','add_time','upd_time']
    model_icon = 'fa fa-handshake-o'


xadmin.site.register(ComInfoModel, ComInfoAdmin)
xadmin.site.register(ComContactModel, ComContactAdmin)
xadmin.site.register(ComRecruitModel, ComRecruitAdmin)
