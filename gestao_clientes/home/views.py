from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View


# Create your views home here.


def home(request):
    return render(request, 'home/home.html')


def my_logout(request):
    logout(request)
    return redirect('home')


class HomePageViews(TemplateView):
    template_name = 'home2.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageViews, self).get_context_data(**kwargs)
        context['variavel'] = 'Olá, seja bem vindo ao curso de Django advanced'
        return context


class MyView(View):

    def get(self, request, *args, **kwargs):
        response = render_to_response('home/home3.html')
        response.set_cookie('color', 'blue', max_age=1000)
        return response

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST')
