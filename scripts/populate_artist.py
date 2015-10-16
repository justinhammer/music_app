#!/usr/bin/env python
import requests
import os, sys
from unidecode import unidecode

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Artists

response = requests.get('https://freemusicarchive.org/api/get/artists.json?api_key=PDCK2LQJIAKLRZFL&limit=3000')
response_dict = response.json()

for data in response_dict['dataset']:
    new_artist, created = Artists.objects.get_or_create(artist_id=int(data.get('artist_id')))
    new_artist.artist_handle = str(data.get('artist_handle'))

    if data.get('artist_url') != None:
        new_artist.artist_url = str(unidecode(data.get('artist_url')))

    if data.get('artist_name') != None:
        new_artist.artist_name = str(unidecode(data.get('artist_name')))

    if data.get('artist_bio') != None:
        new_artist.artist_bio = str(unidecode(data.get('artist_bio')))

    if data.get('artist_members') != None:
        new_artist.artist_members = str(unidecode(data.get('artist_members')))

    if data.get('artist_website') != None:
        new_artist.artist_website = str(unidecode(data.get('artist_website')))

    if data.get('artist_wikipedia_page') != None:
        new_artist.artist_wikipedia_page = str(unidecode(data.get('artist_wikipedia_page')))

    if data.get('artist_donation_url') != None:
        new_artist.artist_donation_url = str(unidecode(data.get('artist_donation_url')))

    if data.get('artist_contact') != None:
        new_artist.artist_contact = str(unidecode(data.get('artist_contact')))

    if data.get('artist_active_year_begin') != None:
        new_artist.artist_active_year_begin = int(unidecode(data.get('artist_active_year_begin')))

    if data.get('artist_active_year_end') != None:
        new_artist.artist_active_year_end = int(unidecode(data.get('artist_active_year_end')))

    if data.get('artist_related_projects') != None:
        new_artist.artist_related_projects = str(unidecode(data.get('artist_related_projects')))

    if data.get('artist_associated_labels') != None:
        new_artist.artist_associated_labels = str(unidecode(data.get('artist_associated_labels')))

    new_artist.artist_comments = str(data.get('artist_comments'))
    new_artist.artist_favorites = str(data.get('artist_favorites'))

    if data.get('artist_date_created') != None:
        new_artist.artist_date_created = str(unidecode(data.get('artist_date_created')))

    new_artist.artist_flattr_name = str(data.get('artist_flattr_name'))
    new_artist.artist_paypal_name = str(data.get('artist_paypal_name'))
    new_artist.artist_latitude = data.get('artist_latitude')
    new_artist.artist_longitude = data.get('artist_longitude')

    new_artist.artist_image_file = str(data.get('artist_image_file'))

    if data.get('artist_location') != None:
        new_artist.artist_location = str(unidecode(data.get('artist_location')))

    print data['artist_id']

    new_artist.save()
