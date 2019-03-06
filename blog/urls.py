from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url('^$', views.post_list, name="post_list"),
    url('^post/(\d+)/$', views.post_detail, name='post_detail'),
    url('^post/new/$', views.post_new, name='post_new'),
    url('post/(\d+)/edit/$', views.post_edit, name='post_edit'),
]
