from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
	path('rss/', views.rss, name='rss'),
    path('rss/load', views.load, name='load')
]