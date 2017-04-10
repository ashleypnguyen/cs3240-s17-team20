from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^userSignup/', views.userSignup),
    url(r'^groupSignup/', views.groupSignup),
    url(r'^uploadReport/', views.uploadReport),
    url(r'^base/', views.base),
    url(r'^showReport/', views.showReport),
    url(r'^groupHome/',views.groupHome),
    url(r'^groupLogin/',views.groupLogin),
]
