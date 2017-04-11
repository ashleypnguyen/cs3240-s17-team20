from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^userSignup/', 'UserGroupForms.views.register', name = 'userSignup'),
    url(r'^groupSignup/', views.groupSignup),
    url(r'^uploadReport/', views.uploadReport),
    url(r'^base/', views.base),
    url(r'^showReport/', views.showReport),
    url(r'^groupHome/',views.groupHome),
    url(r'^groupLogin/',views.groupLogin),
    #url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^confirmUser/',views.confirmUser),

]
