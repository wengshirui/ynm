import xadmin
from xadmin import views
from ynm.models import *


#配置xadmin的全局设置
class BaseSetting(object):
    enable_themes = True   # 打开主题功能
    use_bootswatch = True  #

class Globalsettings(object):
    site_title = "跃农门后台管理系统"  # 系统名称
    site_footer = "跃农门新工人服务平台"  # 底部版权栏
    menu_style = 'accordion' #后台菜单折叠


class BannerAdmin(object):
    '''后台管理前台推荐位的功能'''
    list_display = ['name', 'url', 'desc','add_time', 'upd_time']
    search_fields = ['name', 'url','desc',]
    list_filter = ['name', 'url', 'desc','add_time', 'upd_time']
    model_icon = 'fa fa-newspaper-o'


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, Globalsettings)
