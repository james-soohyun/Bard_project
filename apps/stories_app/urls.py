from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.showUser),
    url(r'^logout', views.logout),
    url(r'^new', views.newStory),
    url(r'^dashboard', views.dashboard),
    url(r'^postStory', views.postStory),
]
