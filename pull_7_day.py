import requests
from requests.auth import HTTPBasicAuth
import json

responsetry = requests.get ('https://api.weather.com/v2/pws/observations/hourly/7day?stationId=KNMLASCR263&format=json&units=e&apiKey=33b111b523f94b80b111b523f9bb80b8', auth=HTTPBasicAuth('KNMLASCR263', 'N2miGFcR'))

print(responsetry.status_code)

print(responsetry.json())


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=False, indent= 4)
    print(text)


jprint(responsetry.json())
