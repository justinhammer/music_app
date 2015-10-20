from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from main.models import Genres, Artists, Albums, Tracks


class GenreListView(ListView):
    model = Genres
    template_name = 'genre_list.html'
    context_object_name = 'genres'


class GenreDetailView(DetailView):
    model = Genres
    slug_field = 'genre_handle'
    template_name = 'genre_detail.html'


class GenreCreateView(CreateView):
    model = Genres
    fields = '__all__'
    template_name = 'genre_create.html'


class ArtistListView(ListView):
    model = Artists
    template_name = 'artist_list.html'
    context_object_name = 'artists'


class ArtistDetailView(DetailView):
    model = Artists
    slug_field = 'artist_name'
    template_name = 'artist_detail.html'


class ArtistCreateView(CreateView):
    model = Artists
    fields = '__all__'
    template_name = 'artist_create.html'


class AlbumListView(ListView):
    model = Albums
    template_name = 'album_list.html'
    context_object_name = 'albums'


class AlbumDetailView(DetailView):
    model = Albums
    slug_field = 'album_title'
    template_name = 'album_detail.html'


class AlbumCreateView(CreateView):
    model = Albums
    fields = '__all__'
    template_name = 'album_create.html'


class TrackListView(ListView):
    model = Tracks
    template_name = 'track_list.html'
    context_object_name = 'tracks'


class TrackDetailView(DetailView):
    model = Tracks
    slug_field = 'track_title'
    template_name = 'track_detail.html'


class TrackCreateView(CreateView):
    model = Tracks
    fields = '__all__'
    template_name = 'track_create.html'
