from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.showProfile),
    url(r'^logout', views.logout),
    url(r'^new', views.newStory),
    url(r'^dashboard', views.dashboard),
    url(r'^postStory', views.postStory),
    url(r'^bardProfile/(?P<user_id>\d+)$', views.bardProfile),
    url(r'^follow/(?P<user_id>\d+)$', views.follow),
    url(r'^unfollow/(?P<user_id>\d+)$', views.unfollow),
]
