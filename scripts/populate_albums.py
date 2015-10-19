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


response = requests.get('https://freemusicarchive.org/api/get/albums.json?api_key=PDCK2LQJIAKLRZFL&limit=3000')

# import ipdb; ipdb.set_trace()
try:
    response_dict = response.json()

    for data in response_dict['dataset']:
        for artist in Artists.objects.all():
            if data.get('album_title') != None and data.get('artist_name') != None and str(unidecode(data.get('artist_name'))) == artist.artist_name:

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
                    album_artist_name, created = Artists.objects.get_or_create(artist_name=data.get('artist_name'))
                    album.album_artist_name = album_artist_name.pk
                except Exception as e:
                    print e

                try:
                    album_image_file = request.get(data.get('album_image_file'))
                    temp_image = NamedTemporaryFile(delete=True)
                    temp_image.write(album_image_file.content)
                    album.album_image_file = File(temp_image)
                except Exception as e:
                    print e

                if new_album.album_title:
                    new_album.save()

except Exception as e:
    print e
    print response
