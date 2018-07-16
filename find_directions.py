from gmap_direction import GmapDirection
import os

key = os.environ.get('SJANG_GOOGLEAPI')
gmap = GmapDirection(key=key)

origin = (37.14979, 129.20528)  # 가곡면사무소
destination = (37.1743125915527, 129.335433959961)  # 호산의원

response = gmap.get_direction(origin, destination)
print(response)


