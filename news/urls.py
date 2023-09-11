from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post/<slug>/', views.news_detail, name="news_detail"),
    path('category/<slug:category_slug>/', views.category_detail, name="category_detail"),
    path('contact/', views.contact, name="contact")
]
