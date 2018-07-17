from datetime import datetime
import requests
import os
import json
from tools import tuple2str, float_trim, list2str


def result2dict(direction_result, num_hosp):
    num_hosp = str(num_hosp)

    ret = dict()
    ret['status' + num_hosp] = direction_result['status']

    if direction_result['status'] != 'OK':
        ret['total_distance' + num_hosp] = -1
        ret['total_duration' + num_hosp] = -1
        ret['end_locations' + num_hosp] = 'None'
        ret['travel_modes' + num_hosp] = 'None'
        ret['distances' + num_hosp] = 'None'
        ret['durations' + num_hosp] = 'None'
        ret['response' + num_hosp] = json.dumps(direction_result)

        return ret

    route = direction_result['routes'][0]['legs'][0]
    total_distance = route['distance']['value'] / 1000  # km
    total_duration = route['duration']['value'] / 1000  # minute

    steps = route['steps']
    end_locations = []
    travel_modes = []
    distances = []
    durations = []

    for step in steps:
        distance = step['distance']['value'] / 1000  # km
        duration = step['duration']['value'] / 60  # minute
        distance = float_trim(distance)
        duration = float_trim(duration)
        end_location = tuple(step['end_location'].values())

        travel_mode = step['travel_mode']
        if travel_mode == 'TRANSIT':
            travel_mode = step['transit_details']['line']['vehicle']['type']

        distances.append(distance)
        durations.append(duration)
        end_locations.append(end_location)
        travel_modes.append(travel_mode)

    ret['total_distance' + num_hosp] = total_distance
    ret['total_duration' + num_hosp] = total_duration
    ret['end_locations' + num_hosp] = list2str(end_locations)
    ret['travel_modes' + num_hosp] = list2str(travel_modes)
    ret['distances' + num_hosp] = list2str(distances)
    ret['durations' + num_hosp] = list2str(durations)
    ret['response' + num_hosp] = json.dumps(direction_result)

    return ret


class GmapDirection:
    def __init__(self, key):
        self.api_url = 'https://maps.googleapis.com/maps/api/directions/json'
        self.departure_time = datetime.strptime(
            "2018-07-16 08:00",
            "%Y-%m-%d %H:%M").timestamp()  # 2018-07-09 08:00
        self.departure_time = int(self.departure_time)

        self.mode = 'transit'
        self.transit_mode = ['bus', 'subway']
        self.region = 'kr'
        self.language = 'ko'

        self.key = key
        self.key = os.environ.get('SJANG_GOOGLEAPI')
        
        self.default_param = {
            'key': self.key,
            'region': self.region,
            'mode': self.mode,
            'trainsit_mode': self.transit_mode,
            'language': self.language,
            'departure_time': self.departure_time
        }

    def get_direction(self, origin, destination):
        self.default_param['origin'] = tuple2str(origin)
        self.default_param['destination'] = tuple2str(destination)

        response = requests.get(self.api_url, params=self.default_param)
        json_dict = response.json()

        return json_dict

    def set_key(self, new_key):
        self.key = new_key

