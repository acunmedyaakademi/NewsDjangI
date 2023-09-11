from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post/<slug>/', views.news_detail, name="news_detail"),

]
