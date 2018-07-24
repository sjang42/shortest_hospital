import requests
from datetime import datetime
import os

# set options for direction
url = 'https://maps.googleapis.com/maps/api/directions/json'  # url to request a directions

departure_time = datetime.strptime(
    "2018-09-03 06:00", "%Y-%m-%d %H:%M").timestamp()  # 2018-07-09 08:00
departure_time = int(departure_time)

origin = '37.14979,129.20528'  # 가곡면사무소
destination = '37.1743125915527, 129.335433959961'  # 호산의원

mode = 'transit'  # available : trainsit(대중교통), walking, bicycling, driving(default)

transit_mode = 'bus|subway|train'  # available : bus, subway, train, tram, rail
region = 'kr'  # ccTLD code
language = 'ko'  # language in which to return results.

# get a key from os environment variable
key = os.environ.get('SJANG_GOOGLEAPI')

# set an option for request
param = {
    'key': key,
    'origin': origin,
    'destination': destination,
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
