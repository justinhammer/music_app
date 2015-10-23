from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from main.models import Genres, Artists, Albums, Tracks, CustomUser
import requests

from main.forms import UserSignUp, UserLogin, ContactForm

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.core.mail import send_mail


def contact_view(request):

    context = {}

    form = ContactForm()

    context['form'] = form

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            send_mail('STATES SITE MESSAGE FROM %s' % name,
                    message,
                    email,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False)
            context['message'] = "email sent"

        else:
            context['message'] = form.errors
    elif request.method == 'GET':
        form = ContactForm()
        context['form'] = form

    return render_to_response('contact_view.html', context, context_instance=RequestContext(request))

def signup(request):

    context = {}

    form = UserSignUp()
    context['form'] = form

    if request.method == 'POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                new_user = CustomUser.objects.create_user(email, password)
                auth_user = authenticate(email=email, password=password)
                login(request, auth_user)
                return HttpResponseRedirect('/')
            except IntegrityError, e:
                context['valid'] = "A User With That Name Already Exists"

        else:
            context['valid'] = form.errors

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/')


def login_view(request):

    context = {}

    context['form'] = UserLogin()

    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            auth_user = authenticate(email=email, password=password)

            if auth_user is not None:
                login(request, auth_user)

                return HttpResponseRedirect('/')
            else:
                context['valid'] = "Invalid User"

        else:
            context['valid'] = "Please enter a User Name"

    return render_to_response('login.html', context, context_instance=RequestContext(request))


class GenreListView(ListView):
    model=Genres
    template_name='genre_list.html'
    context_object_name='genres'


class GenreDetailView(DetailView):
    model=Genres
    slug_field='genre_handle'
    template_name='genre_detail.html'


class GenreCreateView(CreateView):
    model=Genres
    fields='__all__'
    template_name='genre_create.html'


class ArtistListView(ListView):
    model=Artists
    template_name='artist_list.html'
    context_object_name='artists'
    paginate_by = 100


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
    paginate_by = 12


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
    paginate_by = 50


class TrackDetailView(DetailView):
    model = Tracks
    slug_field = 'track_title'
    template_name = 'track_detail.html'


class TrackCreateView(CreateView):
    model = Tracks
    fields = '__all__'
    template_name = 'track_create.html'
