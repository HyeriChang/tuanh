from django.shortcuts import render
from django.views.generic.base import TemplateView
import random

from shop.models import Product
# Create your views here.

class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class MenView(TemplateView):
    template_name = 'men.html'

    def get_context_data(self, **kwargs):
        context = super(MenView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all().filter(is_male=True)
        return context

class WomenView(TemplateView):
    template_name = 'women.html'

    def get_context_data(self, **kwargs):
        context = super(WomenView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all().filter(is_female=True)
        return context


class DetailView(TemplateView):
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        sock_id = kwargs['sock_id']
        context = super(DetailView, self).get_context_data(**kwargs)
        context['sock'] = Product.objects.get(id=sock_id)
        return context

