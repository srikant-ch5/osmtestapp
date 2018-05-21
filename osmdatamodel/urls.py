from django.conf.urls import url,include
from django.contrib import admin
from osmapp import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',include('osmapp.urls')),
    url(r'^stops/',views.get_stops, name="stops"),
    url(r'^osm/', views.load, name="load"),
    url(r'^route_masters', views.get_route_master_relations, name="route_master"),
]
