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

    title='Announcing the go-filecoin alphanet'
    # body='请点击下面链接激活账号：http://127.0.0.1:8000/active/%s' %code
    body="""
    Yesterday, we launched the go-filecoin alphanet, go-filecoin release 0.5.6 (right on schedule – well actually, a day early!). As we announced in our 2019 Q2 & Q3 Update, this was our last major interim milestone before our upcoming testnet launch in December 2019.

The go-filecoin alphanet integrates a number of significant protocol features, but perhaps one of the most important is that it is a long-running network. We launched our first development networks (devnets) earlier this year, but our devnets have not historically included the full machinery for seamless network upgrades. Therefore, whenever we wanted to release new go-filecoin functionality to one of our devnets, we had to trigger a hard network reset. Nodes that were using older go-filecoin versions could no longer connect to the devnets unless they downloaded the latest release and setup their nodes from scratch. Now, with the alphanet launch, we have implemented much of the functionality for seamless network upgrades. While we may still perform hard network resets when necessary, we won’t be required to in order to expose new features to network nodes. This is a major improvement in the realism of our early networks and in the user experience for those who are willing to test them out.

The alphanet release also includes the implementation of several important protocol features, such as:

Our updated Proof-of-Spacetime (PoSt) construction – Rational PoSt
Improvements to our Expected Consensus (EC) algorithm implementation
Drastically faster chainsync, using Graphsync’s IPLD DAG-traversal protocol
New HTTP API design (still WIP)
And more!
A more detailed description of the major changes in this release can be found in our go-filecoin CHANGELOG. (Note: At the time of this writing, the update for release 0.5.6, i.e. the initial alphanet release, is still an open PR in the go-filecoin repo. It should merge shortly.)

Now is as good a time as any to begin testing out the Filecoin protocol implementation and networks. Here are a few pointers for how to get started:

Follow our getting started instructions on our new documentation site to download the latest release and connect to the alphanet.
Check out the activity on our network statistics dashboard.
Join our community chat to ask questions, chat with others in the community, and collaborate on projects
If you are a developer who would like to build projects for the Filecoin ecosystem, please reach out on our discussion forum to add a project to the Filecoin Shipyard and/or apply for a Filecoin dev grant. The deadline for this wave of grant applications is on September 30, 11:59PM PDT.
We’re excited for you to connect to the Filecoin alphanet. Onward!
    """
    ##发送邮件
    """
    subject, message, from_email, recipient_list,
          fail_silently=False, auth_user=None, auth_password=None,
          connection=None, html_message=None
    主题 ，信息，发件人，收件人列表
    """
    send_status=send_mail(title,body,EMAIL_FROM,[email])
    if send_status:
        print('Announcing the go-filecoin alphanet')
        ##返回验证码
        # return code
