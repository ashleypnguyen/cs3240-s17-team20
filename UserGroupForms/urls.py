from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^userSignup/', views.register),
    url(r'^groupSignup/', views.groupSignup),
    url(r'^uploadReport/', views.uploadReport),
    url(r'^base/', views.base),
    url(r'^showReport/', views.showReport),
    url(r'^groupHome/',views.groupHome),
    url(r'^groupLogin/',views.groupLogin),
    #url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login),
    url(r'^confirmUser/',views.confirmUser),
    url(r'^confirmGroup/',views.confirmGroup),
    url(r'^logout/', views.loggingOut),
    url(r'^addUserToGroup/(?P<group_pk>.*)$', views.addUserToGroup, name='addUserToGroup'),
    url(r'^deleteUserFromGroup/(?P<group_pk>.*)$', views.deleteUserFromGroup, name='deleteUserFromGroup'),
    url(r'^search/', views.user_search),
    url(r'^sitemanager/', views.sm),
    url(r'^search/', views.search),
    url(r'^deleteReport/(?P<report_pk>.*)$', views.deleteReport, name='deleteReport'),
    url(r'^fdalogin/$', views.fdalogin),
    url(r'^remote_reports_view/', views.remote_reports_view),
    url(r'^report_info/', views.report_info),
]
