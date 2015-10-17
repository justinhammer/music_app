import requests
import os, sys
from unidecode import unidecode

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Tracks

response = requests.get('https://freemusicarchive.org/api/get/tracks.json?api_key=PDCK2LQJIAKLRZFL&limit=25000')
response_dict = response.json()

