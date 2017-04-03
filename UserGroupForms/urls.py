from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^userSignup/', views.userSignup),
    url(r'^groupSignup/', views.groupSignup),
    url(r'^uploadReport/', views.uploadReport),
    url(r'^base/', views.base),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    #url(r'^showReport/', views.uploadReport),
]