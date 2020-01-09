from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.base, name ="home" ),
    path('donate', views.donate, name = "donate" ),
    path('NewsEvents', views.News_Events, name = "News_Events" ),
    path('campaigns', views.campaign, name="campaign" ),
    path('about', views.about, name="about" ),
    path('thanku/', views.thanku, name='thanku'),
    path('volunteer/', views.volunteer, name='volunteer'),

]
