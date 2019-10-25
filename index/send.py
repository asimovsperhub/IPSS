import random

from django.core.mail import send_mail

from IPSS.settings import EMAIL_FROM
from index.models import EmailRecord

##随机生成验证码
def code_RQ(codelength=8):
    code=''
    str='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    str_len=len(str)-1
    for i  in  range(codelength):
        code+=str[random.randint(0,str_len)]
    return code
# print(code())

##发送邮件
def send_email(email):
    # 实例化models的邮箱验证模块
    email_record=EmailRecord()
    ##将给用户发送的信息保存到数据库中
    ##实例化验证码模块
    code=code_RQ()
    email_record.code=code
    email_record.email=email
    email_record.save()
    ##邮件内容
    ##判断发送邮件的类型

    title='邮箱订阅激活'
    body='请点击下面链接激活账号：http://127.0.0.1:8000/active/%s' %code
    ##发送邮件
    """
    subject, message, from_email, recipient_list,
          fail_silently=False, auth_user=None, auth_password=None,
          connection=None, html_message=None
    主题 ，信息，发件人，收件人列表
    """
    send_status=send_mail(title,body,EMAIL_FROM,[email])
    if send_status:
        print('注册邮件发送成功')
        ##返回验证码
        # return code
