from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('article/', views.blog_list, name='blog_list'),
    path('article/create/', views.blog_create, name='blog_create'),
]
