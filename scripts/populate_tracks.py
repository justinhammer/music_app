#!usr/bin/env python
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

from main.models import Albums, Artists, Genres, Tracks

django.setup()

response = requests.get('https://freemusicarchive.org/api/get/tracks.json?api_key=PDCK2LQJIAKLRZFL&limit=25000')

try:
    response_dict = response.json()

    for data in response_dict['dataset']:
        new_track, created = Tracks.objects.get_or_create(track_id=int(data.get('track_id')))

        if data.get('track_title') != None:
            new_track_title = str(unidecode(data.get('track_title')))

        if data.get('track_url') != None:
            new_track_url = str(unidecode(data.get('track_url')))

        if data.get('license_title') != None:
            new_license_title = str(unidecode(data.get('license_title')))

        if data.get('license_url') != None:
            new_license_url = str(unidecode(data.get('license_url')))

        if data.get('track_language_code') != None:
            new_track_language_code = str(unidecode(data.get('new_track_language_code')))

        if data.get('track_duration') != None:
            new_track_duration = str(unidecode(data.get('new_track_duration')))

        new_track_number = int(data.get('track_number'))
        new_track_disc_number = int(data.get('track_disc_number'))

        if data.get('track_explicit') != None:
            new_track_explicit = str(unidecode(data.get('track_explicit')))

        if data.get('track_explicit_notes') != None:
            new_track_exlpicit_notes = str(unidecode(data.get('track_explicit_notes')))

        if data.get('track_copyright_c') != None:
            new_track_copyright_c = str(unidecode(data.get('track_copyright')))

        if data.get('track_copyright_p') != None:
            new_track_copyright_d = str(unidecode(data.get('track_copyright_d')))

        if data.get('track_composer') != None:
            new_track_composer = str(unidecode(data.get('track_composer')))

        if data.get('track_lyricist') != None:
            new_track_lyricist = str(unidecode(data.get('track_lyricist')))

        if data.get('track_publisher') != None:
            new_track_publisher = str(unidecode(data.get('track_publisher')))

        new_track_instrumental = int(data.get('track_instrumental'))

        if data.get('track_information') != None:
            new_track_information = str(unidecode(data.get('track_information')))

        if data.get(track_date_recorded) != None:
            new_track_date_recorded = str(unidecode(data.get('track_date_recorded')))

        if data.get('track_comments') != None:
            new_track_comments = str(unidecode(data.get('track_comments')))

        new_track_favorites = int(data.get('track_favorites'))
        new_track_listens = int(data.get('track_listens'))
        new_track_interest = int(data.get('track_interest'))
        new_track_bit_rate = int(data.get('track_bit_rate'))

        if data.get('track_date_created') != None:
            new_track_date_created = str(unidecode(data.get('track_date_created')))

        if data.get('track_file') != None:
            new_track_file = str(unidecode(data.get('track_file')))

        try:
            album, created = Albums.objects.get_or_create(album_id=data.get('album_id'))
            track.album = album_id.pk
        except Exception as e:
            print e

        try:
            track_image_file = request.get(data.get('track_image_file'))
            temp_image = NamedTemporaryFile(delete=True)
            temp_image.write(track_image_file.content)
            track.track_image_file = File(temp_image)
        except Exception as e:
            print e

        try:
            license_image_file = request.get(data.get('license_image_file'))
            temp_image = NamedTemporaryFile(delete=True)
            temp_image.write(license_image_file.content)
            track.license_image_file = File(temp_image)
        except Exception as e:
            print e

        try:
            license_image_file_large = request.get(data.get('license_image_file_large'))
            temp_image - NamedTemporaryFile(delete=True)
            temp_image.write(license_image_file_large.content)
            track.license_image_file_large = File(temp_image)
        except Exception as e:
            print e



