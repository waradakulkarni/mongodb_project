"""mongoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('business/top/', views.business_top, name='business_top'),
    path('business/happyhour/', views.business_happyhour, name='business_top'),
    path('business/<id>/open/<open>/', views.business_isopen, name='business_isopen'),
    path('business/<id>/delete', views.business_delete, name='business_delete'),
    path('reviews/insert/', views.reviews_insert, name='reviews_insert'),

]
