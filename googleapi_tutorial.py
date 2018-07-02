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
departure_time = datetime.strptime("2018-06-28 14:00",
                                   "%Y-%m-%d %H:%M")  # 2018-06-28 14:00
mode = 'transit'
transit_mode = ['bus', 'subway', 'train', 'tram', 'rail',
                'rail']  # all transits available
region = 'kr'

# Request distance via public transit
distance_result = gmaps.distance_matrix(
    origins=origin,
    destinations=destination,
    mode=mode,
    transit_mode=transit_mode,
    region=region,
    departure_time=departure_time)

# Print result
print(distance_result)
for key, value in distance_result.items():
    print('{} : {}'.format(key, value))
