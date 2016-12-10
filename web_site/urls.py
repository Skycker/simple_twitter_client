# coding: utf-8
from django.conf.urls import url

from web_site import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
]
