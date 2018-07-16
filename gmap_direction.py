from datetime import datetime
import requests
import os
from tools import tuple2str


class GmapDirection:
    def __init__(self, key):
        self.api_url = 'https://maps.googleapis.com/maps/api/directions/json'
        self.departure_time = datetime.strptime("2018-07-16 08:00",
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
