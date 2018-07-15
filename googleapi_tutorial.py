from datetime import datetime
import googlemaps
import os

# Take key from environment variable and make instance
key = os.environ.get('SJANG_GOOGLEAPI')
gmaps = googlemaps.Client(key=key)

# Set origin and destination
origin = (37.14979, 129.20528)  # 가곡면사무소
destination = (37.1743125915527, 129.335433959961)  # 호산의원

# Set options for distance
departure_time = datetime.strptime("2018-07-09 08:00",
                                   "%Y-%m-%d %H:%M")  # 2018-07-09 08:00
mode = 'transit'
transit_mode = ['bus', 'subway']
region = 'kr'

# Request distance via public transit
distance_result = gmaps.distance_matrix(
    origins=origin,
    destinations=destination,
    mode=mode,
    transit_mode=transit_mode,
    region=region,
    departure_time=departure_time)

# Request direction via public transit
direction_result = gmaps.directions(
    origin=origin,
    destination=destination,
    mode=mode,
    transit_mode=transit_mode,
    region=region,
    departure_time=departure_time)

steps = direction_result[0]['legs'][0]['steps']

print('--distance_result--')
for key, value in distance_result.items():
    print('{} : {}'.format(key, value))

print('')
print('--direction result--')
for step in steps:
    print(step['html_instructions'],
          '(' + '{0:0.1f}'.format(step['distance']['value'] * 0.001) + 'km, ' +
          str(step['duration']['value']) + 'min)')
