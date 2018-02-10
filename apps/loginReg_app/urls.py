from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^register$', views.register),
    url(r'^createUser$', views.createUser),
    url(r'^login$', views.login),
]
