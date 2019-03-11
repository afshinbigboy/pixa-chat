from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^user_list/', views.user_list, name='user_list'),
    url(r'^$', views.index, name='index'),
    url(r'^rooms$', views.room_list, name='room'),
    url(r'^rooms/(?P<room_name>[^/]+)/$', views.room, name='room'),
]

