from django.urls import path
from .views import home, my_logout, HomePageViews, MyView
from django.views.generic.base import TemplateView


app_patterns = 'home'
urlpatterns = [
    path('', home, name='home'),
    path('logout/', my_logout, name='logout'),
    path('home2/', TemplateView.as_view(template_name='home2.html')),
    path('home3/', HomePageViews.as_view(template_name='home3.html')),
    path('view/', MyView.as_view()),
]