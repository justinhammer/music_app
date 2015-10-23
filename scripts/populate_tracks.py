#!/usr/bin/env python
import requests
import os, sys
from unidecode import unidecode
from PIL import Image

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from main.models import Albums, Artists, Tracks

django.setup()

response = requests.get('https://freemusicarchive.org/api/get/tracks.json?api_key=PDCK2LQJIAKLRZFL&limit=5000')
Tracks.objects.all().delete()

try:
    response_dict = response.json()

    for data in response_dict['dataset']:
        for alb in Albums.objects.all():
            if data.get('track_title') != None and data.get('album_title') != None and str(unidecode(data.get('album_title'))) == alb.album_title:

                new_track, created = Tracks.objects.get_or_create(track_id=int(data.get('track_id')))

                if data.get('track_title') != None:
                    new_track.track_title = str(unidecode(data.get('track_title')))

                if data.get('track_url') != None:
                    new_track.track_url = str(unidecode(data.get('track_url')))

                if data.get('license_title') != None:
                    new_track.license_title = str(unidecode(data.get('license_title')))

                if data.get('license_url') != None:
                    new_track.license_url = str(unidecode(data.get('license_url')))

                if data.get('track_language_code') != None:
                    new_track.track_language_code = str(data.get('new_track_language_code'))

                if data.get('track_duration') != None:
                    new_track.track_duration = str(data.get('new_track_duration'))

                new_track.track_number = int(data.get('track_number'))
                new_track.track_disc_number = int(data.get('track_disc_number'))

                if data.get('track_explicit') != None:
                    new_track.track_explicit = str(unidecode(data.get('track_explicit')))

                if data.get('track_explicit_notes') != None:
                    new_track.track_exlpicit_notes = str(unidecode(data.get('track_explicit_notes')))

                if data.get('track_copyright_c') != None:
                    new_track.track_copyright_c = str(unidecode(data.get('track_copyright_c')))

                if data.get('track_copyright_p') != None:
                    new_track.track_copyright_d = str(data.get('track_copyright_d'))

                if data.get('track_composer') != None:
                    new_track.track_composer = str(unidecode(data.get('track_composer')))

                if data.get('track_lyricist') != None:
                    new_track.track_lyricist = str(unidecode(data.get('track_lyricist')))

                if data.get('track_publisher') != None:
                    new_track.track_publisher = str(unidecode(data.get('track_publisher')))

                new_track.track_instrumental = int(data.get('track_instrumental'))

                if data.get('track_information') != None:
                    new_track.track_information = str(unidecode(data.get('track_information')))

                if data.get('track_date_recorded') != None:
                    new_track.track_date_recorded = str(unidecode(data.get('track_date_recorded')))

                if data.get('track_comments') != None:
                    new_track.track_comments = str(unidecode(data.get('track_comments')))

                new_track.track_favorites = int(data.get('track_favorites'))
                new_track.track_listens = int(data.get('track_listens'))
                new_track.track_interest = int(data.get('track_interest'))

                if data.get('track_bit_rate') != None:
                    new_track.track_bit_rate = int(data.get('track_bit_rate'))

                if data.get('track_date_created') != None:
                    new_track.track_date_created = str(unidecode(data.get('track_date_created')))

                if data.get('track_file') != None:
                    new_track.track_file = str(unidecode(data.get('track_file')))

                new_track.album = alb

                try:
                    new_track_image_file = requests.get(data.get('track_image_file'))
                    temp_image = NamedTemporaryFile(delete=True)
                    temp_image.write(new_track_image_file.content)
                    img_name = "%s_track_image_file.jpg" % new_track.track_id
                    new_track.track_image_file.save(img_name, File(temp_image))
                except Exception as e:
                    print new_track.track_id
                    print e

                try:
                    new_license_image_file = requests.get(data.get('license_image_file'))
                    temp_image = NamedTemporaryFile(delete=True)
                    temp_image.write(new_license_image_file.content)
                    img_name = "%s_license_image_file.jpg" % new_track.track_id
                    new_track.license_image_file.save(img_name, File(temp_image)) 
                except Exception as e:
                    print new_track.track_id
                    print e

                try:
                    new_license_image_file_large = requests.get(data.get('license_image_file_large'))
                    temp_image = NamedTemporaryFile(delete=True)
                    temp_image.write(new_license_image_file_large.content)
                    img_name = "%s_license_image_file_large.jpg" % new_track.track_id
                    new_track.license_image_file_large.save(img_name, File(temp_image))
                except Exception as e:
                    print new_track.track_id
                    print e

                new_track.save()

            else:
                pass

except Exception as e:
    print e
    print response
