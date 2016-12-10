# coding: utf-8
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from web_site import models


class IndexView(generic.TemplateView):
    template_name = "web_site/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['after_login_url'] = reverse("web_site:followers")
        return context


class FollowerListView(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('web_site:index')
    template_name = "web_site/followers.html"
    context_object_name = 'followers'

    def get_queryset(self):
        qs = models.Follower.objects.filter(user=self.request.user)
        q = self.request.GET.get('q', None)
        if q:
            return qs.filter(screen_name__icontains=q)
        return qs

    def get_context_data(self, **kwargs):
        cd = super(FollowerListView, self).get_context_data(**kwargs)
        cd['q'] = self.request.GET.get('q', '')
        return cd


class FollowerDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = reverse_lazy('web_site:index')
    template_name = 'web_site/follower.html'
    context_object_name = 'follower'
    model = models.Follower


class RemoveAccountView(LoginRequiredMixin, generic.View):
    login_url = reverse_lazy('web_site:index')

    def post(self, *args, **kwargs):
        self.request.user.delete()
        return HttpResponseRedirect(reverse("web_site:index"))
