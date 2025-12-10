from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('contact/', views.contact),
    path('about/', views.about),
    path('login/', views.login),
    path('register/', views.register)
]
