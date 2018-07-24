import requests
from datetime import datetime
from tools import tuple2str
import os

# Set options for direction
url = 'https://maps.googleapis.com/maps/api/directions/json'

departure_time = datetime.strptime(
    "2018-07-09 08:00", "%Y-%m-%d %H:%M").timestamp()  # 2018-07-09 08:00
departure_time = int(departure_time)

origin = (37.14979, 129.20528)  # 가곡면사무소
destination = (37.1743125915527, 129.335433959961)  # 호산의원

mode = 'transit'
transit_mode = 'bus|subway|train'
region = 'kr'
language = 'ko'

# get a key from os environment variable
key = os.environ.get('SJANG_GOOGLEAPI')

# set an option for request
param = {
    'key': key,
    'origin': tuple2str(origin),
    'destination': tuple2str(destination),
    'region': region,
    'mode': mode,
    'transit_mode': transit_mode,
    'language': language,
    'departure_time': departure_time
}

# send a request to google
response = requests.get(url, params=param)

# convert response to json format
json_dict = response.json()

# print response as json formats
print(json_dict)
