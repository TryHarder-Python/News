from django.urls import path
from . import views

urlpatterns = [
    path("", views.news_list, name='home'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('category/<int:category_id>/', views.news_category, name='news_categories'),
    path('news/add-newspopa', views.news_add, name='news_add')
]