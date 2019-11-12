from django.contrib import admin

# Register your models here.
from index.models import Blogs, Photo, Upload


##注册博客后台模型
class   BlogAdmin(admin.ModelAdmin):
    list_display = ['label','title','header','src','content']
    search_fields = ['title']
    list_filter = ['id']
admin.site.register(Blogs,BlogAdmin)

##gif图
class   PhotoAdmin(admin.ModelAdmin):
    ##定义后台列表展示的字段
    list_display = ['title','position','src','href']
    ##定义后台允许搜索的字段
    search_fields = ['title']
    ##后台过滤器，筛选字段
    list_filter = ['position']

# admin.register(Photo,PhotoAdmin)数据模型，admin类
#注册后台功能
admin.site.register(Photo,PhotoAdmin)

class   UploadAdmin(admin.ModelAdmin):
    list_display = ['filename','file_upload','file_type']
    search_fields = ['fielname']
    list_filter = ['filename']
admin.site.register(Upload,UploadAdmin)