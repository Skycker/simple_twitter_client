# coding: utf-8
from django.conf.urls import url

from web_site import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^followers$', views.FollowerListView.as_view(), name="followers"),
    url(r'^followers/(?P<pk>[0-9]+)$', views.FollowerDetailView.as_view(), name="follower"),
    url(r'^remove$', views.RemoveAccountView.as_view(), name="remove"),
]
