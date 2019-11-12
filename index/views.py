import json
import re
import traceback

from django.http import StreamingHttpResponse, JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from index.models import Blogs, Photo, User, EmailRecord, Upload
from index.send import send_email

#主页
def index(request):
    #
    photos = Photo.objects.all().order_by('position')
    files = Upload.objects.all().order_by('filename')
    # file_types = Upload.objects.all().order_by('file_type')
    # if request.method == 'GET':
    inputMail = request.GET.get('email', '')
    print(inputMail)
    ##验证邮箱的合法性
    isMatch = bool(
        re.match(r"^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$",
                 inputMail, re.VERBOSE))
    #print(isMatch)
    if isMatch:
        ##邮箱去重
        is_email_exist = User.objects.filter(email=inputMail).exists()
        if  is_email_exist:
            # ret=0
            # return HttpResponse(json.dumps({
            #     "ret": ret,
            # }))
            status=send_email(inputMail)
            if status:
                print("邮件发送成功")

        else:
            ##实例化用户表
            user_profile = User()
            user_profile.email = inputMail
            user_profile.is_activate = False
            user_profile.save()
            ##发送邮件
            #status = send_email(inputMail)
            #mess="订阅成功，我们将给你邮箱发送激活链接，注意查收"
            status = send_email(inputMail)
            if status:
                print("邮件发送成功")
    # else:
    #     mess = "邮箱格式不正确"
    return render(request,'index.html',locals())
##激活邮箱
def ActiveUser(request,active_code):
    ##在数据库中查询用户访问的这个邮箱激活码
    all_record=EmailRecord.objects.filter(code=active_code)
    if  all_record:
        for cord in all_record:
            ##通过这个邮箱验证码找到EmailRecord的email
            email=cord.email
            ##通过email这个找到User的email(因为先注册后邮箱验证，传的值是同一个email)
            user=User.objects.get(email=email)
            ##将用户的状态改为激活状态
            user.is_active=1
            user.save()
            mess="激活成功，以后我们会将关于IPSS的最新信息发送到你的邮箱"
        return render(request,'index.html',locals())   ##locals()显示当前函数所有局部变量

def sendblogEmail(request):
    pass


def  download(request):
    # if request.method == 'GET':
        # def file_iterator(file_name, chunk_size=512):
        #     with open(file_name) as f:
        #         while True:
        #             c = f.read(chunk_size)
        #             if c:
        #                 yield c
        #             else:
        #                 break
        ##从前端传入的文件名
        filename=request.GET.get('filename')
        #print(filename)
        the_file_name = open("/Users/apple/PycharmProjects/IPSS/static/media/%s" %filename, 'rb')
        file_name=str(the_file_name).split('/')[-1].split("'")[0]
        response = StreamingHttpResponse(the_file_name)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
        # print(response.streaming_content)
        return response
##后台

def blog(request):
    blogs = Blogs.objects.all().order_by('id')

    data = {
        'blogs': blogs,
    }
    ##给前台传入所有的blogs的数据

    return render(request,'blog.html',locals())

def blogcontent(request,label):
    blogs=Blogs.objects.filter(label=label)
    print(blogs)
    data = {
        'blogs': blogs,

    }
    return render(request,'blogcontent.html',locals())

def gif(request):
    # 轮播图显示给前端
    photo = Photo.objects.all().order_by('position')
    data = {
        'photos': photo,

    }
    ##给前台传入所有的photo数据
    return render(request, 'index.html', locals())
