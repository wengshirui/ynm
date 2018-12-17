__author__ = 'wsr'
__date__ = '2018/11/9 0009 下午 4:19'

'''这个py文件是用来发送验证邮件的，比如注册验证、找回密码等，目前这个功能都被手机短信做了，此处待定'''
'''该干的活还是要干的，偷懒是解决不了问题的'''

from ynm.models import EmailVerifyRecord
import random
from django.core.mail import send_mail
from untitled2.settings import *

def send_email(email,send_type='forget'):
    email_record = EmailVerifyRecord()
    email_record.code = random.randint(100000,999999) #暂未考虑随机数重复的问题
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'forget':
        email_title = '找回密码'
        email_body = '请点击以下链接找回您的密码：'

        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
