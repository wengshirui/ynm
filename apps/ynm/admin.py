from django.contrib import admin

# Register your models here.
'''
    '1 创建django项目
    '2 创建app 
    '3 关联数据库，并迁移 makemigration migrate
    '4 创建超级用户 admin admin123456
    '5 根据需求创建url html页面 和业务操作逻辑 view  数据库操作model
    '6 根据需求使用第三方app如xadmin或创建表单验证等
    '7 做好相关设置如static文件 上传文件media等
'''

'''
    工人：基本信息，在职情况，技能情况
    岗位：名称，要求，所需技能及等级
    技能：等级，等级划分标准
    公司：所需岗位，薪酬待遇，联系人，联系方式，地址，公司介绍
    中介：
    平台用户：工号，姓名，邮箱，联系方式，权限
    服务；
    服务订单：工人 服务内容 供应商 下单时间  服务时间  订单金额  促销金额  实付金额
    供应商：

'''
#工作的核心不是找到大公司，拿到高工资，是工作的有尊严，享受工作，除了合适的条件还有更多的尊重和希望

# 表model  后台样式adminx  业务逻辑URL，view  前台样式template