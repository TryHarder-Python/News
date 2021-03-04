from django.urls import path
from . import views

urlpatterns = [
    path("", views.news_list, name='home'),
    path('news/<str:slug>', views.news_detail, name='news_detail')
]