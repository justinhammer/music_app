#!/usr/bin/env python
import requests
import os, sys
from unidecode import unidecode
from PIL import Image
from StringIO import StringIO

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from main.models import Albums, Artists, Genres

django.setup()

Albums.objects.all().delete()
artists_in_db = Artists.objects.all()

for artist in artists_in_db:
    albums_url = "https://freemusicarchive.org/api/get/albums.json?api_key=PDCK2LQJIAKLRZFL&artist_id="
    current_artist_id = str(artist.artist_id)
    url_w_artist_id = str(albums_url) + current_artist_id
    response = requests.get(url_w_artist_id)
    response_dict = response.json()

    for data in response_dict['dataset']:

            new_album, created = Albums.objects.get_or_create(album_id=int(data.get('album_id')))

            if data.get('album_title') != None:
                new_album.album_title = str(unidecode(data.get('album_title')))

            if data.get('album_handle') != None:
                new_album.album_handle = str(unidecode(data.get('album_handle')))

            if data.get('album_url') != None:
                new_album.album_url = str(unidecode(data.get('album_url')))

            if data.get('album_type') != None:
                new_album.album_type = str(unidecode(data.get('album_type')))

            if data.get('album_producer') != None:
                new_album.album_producer = str(unidecode(data.get('album_producer')))

            if data.get('album_engineer') != None:
                new_album.album_engineer = str(unidecode(data.get('album_engineer')))

            if data.get('album_information') != None:
                new_album.album_information = str(unidecode(data.get('album_information')))

            if data.get('album_date_released') != None:
                new_album.album_date_released = str(unidecode(data.get('album_date_released')))

            new_album.album_comments = int(data.get('album_comments'))
            new_album.album_favorites = int(data.get('album_favorites'))
            new_album.album_tracks = int(data.get('album_tracks'))
            new_album.album_listens = int(data.get('album_listens'))

            if data.get('album_date_created') != None:
                new_album.album_date_created = str(unidecode(data.get('album_date_created')))

            try:
                new_album.album_artist_id = Artists.objects.get(artist_id=current_artist_id)
            except Exception, e:
                new_album.album_artist_id = None

            # try:
            #     album_artist_name, created = Artists.objects.get_or_create(artist_name=data.get('artist_name'))
            #     album.album_artist_name = album_artist_name.pk
            # except Exception as e:
            #     print e

            try:
                new_album_image = requests.get(data.get('album_image_file'))
                temp_image = NamedTemporaryFile(delete=True)
                temp_image.write(new_album_image.content)
                img_name = "%s_album_img.jpg" % new_album.album_id
                new_album.album_image_file.save(img_name, File(temp_image))
            except Exception as e:
                print "no image %s" % new_album.album_id
                print e

            new_album.save()
