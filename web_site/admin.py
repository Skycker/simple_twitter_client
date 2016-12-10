# coding: utf-8
from django.contrib import admin

from web_site import models


@admin.register(models.Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ("full_screen_name", 'user', 'name', 'lang', 'followers_count')
    search_fields = ("screen_name", 'name')
