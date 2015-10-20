"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from main import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^genre_list/$', views.GenreListView.as_view()),
    url(r'^genre_detail/(?P<slug>.+)/$', views.GenreDetailView.as_view()),
    url(r'^genre_create/$', views.GenreCreateView.as_view()),
    url(r'^album_list/$', views.AlbumListView.as_view()),
    url(r'^album_detail/(?P<slug>.+)/$', views.AlbumDetailView.as_view()),
    url(r'^album_create/$', views.AlbumCreateView.as_view()),
    url(r'^artist_list/$', views.ArtistListView.as_view()),
    url(r'^artist_detail/(?P<slug>.+)/$', views.ArtistDetailView.as_view()),
    url(r'^artist_create/$', views.ArtistCreateView.as_view()),
    url(r'^track_list/$', views.TrackListView.as_view()),
    url(r'^track_detail/(?P<slug>.+)/$', views.TrackDetailView.as_view()),
    url(r'^track_create/$', views.TrackCreateView.as_view()),
]
