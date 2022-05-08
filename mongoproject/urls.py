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
    path('business/top/', views.business_top, name='business_top'), #Use Case 2
    path('business/happyhour/', views.business_happyhour, name='business_happyhour'), #Use Case 3
    path('business/<id>/open/<open>/', views.business_isopen, name='business_isopen'), #Use Case 6
    path('business/<id>/delete', views.business_delete, name='business_delete'), #Use Case 9
    path('reviews/insert/', views.reviews_insert, name='reviews_insert'), #Use Case 5
    path('business/<id>/', views.business_find, name='business_find'),
    path('reviews/<id>/', views.review_find, name='review_find'),
    path('business/topten/<zipcode>/', views.business_find_topten, name='business_find_topten'), #Use Case 1
    path('business/category/<cat>/', views.business_category, name='business_category'), #Use Case 4
    path('business/timing/<name>/', views.business_display_timings, name='business_display_timings'), #Use Case 7
    path('business/<id>/latestreview/', views.business_display_latestreview, name='business_display_latestreview'), #Use Case 8
    path('business/attribute/takeoutone/', views.business_takeout_one, name='business_takeout_one'), #Use Case 10
    path('business/avg_rating/city/<city>/', views.business_avgrating_city, name='business_avgrating_city'), #Use Case 11
    path('business/avg_rating/state/<state>/', views.business_avgrating_state, name='business_avgrating_state'), #Use Case 12
    path('business/search/<keyword>/', views.business_keyword_search, name='business_keyword_search'), #Use Case 13
    path('business/<id>/longestreview/', views.business_display_longestreview, name='business_display_longestreview'), #Use Case 14
    path('business/check/openonMonday/', views.business_openday, name='business_openday') #Use Case 15
]
