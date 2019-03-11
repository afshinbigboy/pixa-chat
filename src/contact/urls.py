from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^list/', views.list, name='list'),
    # url(r'^chat/(?P<room_name>[^/]+)/$', views.room, name='room'),
]

