from django.conf.urls import url
from django.urls import path

from index import views

urlpatterns=[
    path('', views.index, name='index'),
    #url(r'',views.index,name='index')
    path('Blod/',views.blod,name='blod'),
    ##邮箱激活
    path('active/<str:active_code>',views.ActiveUser,name='activeuser'),
    ##dowmload
    url(r'^download/',views.download,name='download'),
    path('index/',views.index,name='index')
]