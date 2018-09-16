import xadmin
from xadmin import views


#配置xadmin的全局设置
class BaseSetting(object):
    enable_themes = True   # 打开主题功能
    use_bootswatch = True  #

class Globalsettings(object):
    site_title = "跃农门后台管理系统"  # 系统名称
    site_footer = "跃农门新工人服务平台"  # 底部版权栏

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, Globalsettings)
