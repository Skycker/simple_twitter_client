# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 17:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_id', models.BigIntegerField(verbose_name='Twitter account id')),
                ('screen_name', models.CharField(db_index=True, max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('followers_count', models.IntegerField(default=0, verbose_name='Number of followers')),
                ('lang', models.CharField(max_length=3, verbose_name="Follower's language")),
                ('image_url', models.URLField(blank=True, max_length=300, verbose_name="Follower's profile image URL")),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
