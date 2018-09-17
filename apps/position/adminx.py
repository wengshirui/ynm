import xadmin
from .models import TradeModel,PositionModel,SkillModel


#配置后台显示/搜索/过滤字段
class TradeAdmin(object):
    list_display = ['name', 'example', 'desc', 'add_time','upd_time']
    search_fields = ['name', 'example','desc']
    list_filter = ['name', 'example', 'desc', 'add_time','upd_time']
    model_icon = 'fa fa-globe'


class PositionAdmin(object):
    list_display = ['name', 'desc', 'skill','add_time','upd_time']
    search_fields = ['name', 'desc', 'skill']
    list_filter = ['name', 'desc', 'skill', 'add_time','upd_time']
    model_icon = 'fa fa-street-view'


class SkillAdmin(object):
    list_display = ['name', 'grade', 'desc','add_time', 'upd_time']
    search_fields = ['name', 'grade','desc',]
    list_filter = ['name', 'grade', 'desc','add_time', 'upd_time']
    model_icon = 'fa fa-wrench'


xadmin.site.register(TradeModel, TradeAdmin)
xadmin.site.register(PositionModel, PositionAdmin)
xadmin.site.register(SkillModel, SkillAdmin)