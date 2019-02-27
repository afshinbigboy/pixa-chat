from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^sign-in/', views.sign_in, name='sign_in'),
    url(r'^sign-out/', views.sign_out, name='sign_out'),
    url(r'^sign-up/', views.sign_up, name='sign_up'),
]