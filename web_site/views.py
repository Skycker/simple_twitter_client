# coding: utf-8
from django.urls import reverse
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "web_site/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['after_login_url'] = reverse("web_site:index")
        return context