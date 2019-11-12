# from datetime import datetime
import datetime

from django.db import models

# Create your models here.

##用户表

class   User(models.Model):
    email=models.EmailField(max_length=50,verbose_name='邮箱')
    is_active=models.BooleanField(default=False)



##邮箱订阅验证
class   EmailRecord(models.Model):
    code=models.CharField(max_length=20,verbose_name='验证码')
    ##
    email=models.EmailField(max_length=50,verbose_name='邮箱')
    ##订阅时间
    send_time=models.DateTimeField(verbose_name='发送时间',default=datetime.datetime.now)




######################    后台数据模型

##添加代码gif
class   Photo(models.Model):
    title = models.CharField(max_length=20, verbose_name='轮播图标题')
    href = models.CharField(max_length=300, verbose_name='图片广告链接')
    ##upload_to图片上传后存储的目录，如果不存在则会自动创建
    src = models.ImageField(upload_to="static/img/banner/", verbose_name='图片')
    position = models.IntegerField(verbose_name='顺序', choices=(
        (1, 'new'),
        (2, 'old')), default=1)

    class Meta:
        # db_table   指定数据表名称
        db_table = 'Photo'
        ##复数
        verbose_name = '代码gif'
        ##复数->单数
        verbose_name_plural = verbose_name

    ##按照自定义的格式输出内容
    def __str__(self):
        return self.title
##上传安装包
class Upload(models.Model):
    filename = models.CharField(max_length=20, verbose_name='filename')
    file_upload = models.FileField(upload_to='static/media')
    file_type = models.IntegerField(verbose_name='安装包类型', choices=(
        (0, 'Windows'),
        (1, 'Linux'),
        (2, 'Android')), default=0)

    class Meta:
        # db_table   指定数据表名称
        db_table = 'Upload'
        ##复数
        verbose_name = '上传安装包'
        ##复数->单数
        verbose_name_plural = verbose_name

##后台添加博客数据模型

class Blogs(models.Model):
    ##

    label = models.CharField(max_length=200, verbose_name='博客标签')
    title = models.CharField(max_length=200, verbose_name='博客标题')
    header = models.TextField(verbose_name='博客简介')
    ##upload_to图片上传后存储的目录，如果不存在则会自动创建
    src = models.ImageField(upload_to="static/img/banner/", verbose_name='图片',default=0)
    content=models.TextField(verbose_name='博客内容',default=0)

    # readcount=models.IntegerField(verbose_name='阅读量')
    class Meta:
        # db_table   指定数据表名称
        db_table = 'blogs'
        ##复数
        verbose_name = '添加博客'
        ##复数->单数
        verbose_name_plural = verbose_name

    ##按照自定义的格式输出内容
    def __str__(self):
        return self.title
