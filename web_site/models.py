# coding: utf-8
from __future__ import unicode_literals

import tweepy
from allauth.account.signals import user_signed_up
from allauth.socialaccount.models import SocialApp
from django.conf import settings
from django.db import models
from django.urls import reverse


# One twitter account can follow two ore more users.
# So, better way is to make many-to-many relationship between Follower model and AUTH_USER_MODEL
class Follower(models.Model):
    """ User's twitter followers list """

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    twitter_id = models.BigIntegerField(verbose_name='Twitter account id')
    screen_name = models.CharField(max_length=128, db_index=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    followers_count = models.IntegerField(verbose_name='Number of followers', default=0)
    lang = models.CharField(max_length=3, verbose_name="Follower's language")
    image_url = models.URLField(blank=True, max_length=300, verbose_name="Follower's profile image URL")

    @property
    def full_screen_name(self):
        return "@{0}".format(self.screen_name)

    def get_absolute_url(self):
        return reverse("web_site:follower", kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.full_screen_name


# better approach is synchronization followers asynchronously. I will reduce time user waiting after registration.
# Extra http requests to Twitter take time and suffer from possible network connection problems
# Run async task just after registration and run it periodically to load new followers
def sync_followers(request, user, **kwargs):
    """ Sync user's followers after sign up """

    social_login = kwargs['sociallogin']
    consumer_key = social_login.token.app.client_id
    consumer_secret = social_login.token.app.secret
    access_token = social_login.token.token
    access_token_secret = social_login.token.token_secret

    auth_handler = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_handler.set_access_token(access_token, access_token_secret)
    twitter_api = tweepy.API(auth_handler)

    followers = []
    for follower in tweepy.Cursor(twitter_api.followers).items():
        followers.append(
            Follower(user=user, twitter_id=follower.id, screen_name=follower.screen_name, name=follower.name,
                     description=follower.description, image_url=follower.profile_image_url,
                     followers_count=follower.followers_count, lang=follower.lang,
                     )
        )
    Follower.objects.bulk_create(followers, batch_size=100)


user_signed_up.connect(sync_followers)
