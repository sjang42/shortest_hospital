from gmap_direction import GmapDirection, result2dict
from openpyxl import Workbook

from tools import excel_to_dict, is_excel
import os

key = os.environ.get('SJANG_GOOGLEAPI')
gmap = GmapDirection(key=key)

in_dirname = './straight/'
straight = os.listdir(in_dirname)

num_find = 3
# todo : key 제한 걸고 loop 돌기

for f in straight:
    if not is_excel(f):
        continue

    fname = os.path.join(in_dirname, f)
    print(fname)
    offices = excel_to_dict(fname, mute=False)

    wb = Workbook()
    ws = wb.active

    for i, office in enumerate(offices):
        origin = (office['Y'], office['X'])
        print(office)
        for num in range(num_find):
            destination = (office['Y_hosp' + str(num + 1)], office['X_hosp' + str(num + 1)])
            direction_result = gmap.get_direction(origin, destination)
            direction_dict = result2dict(direction_result, num + 1)
            print(direction_dict)
        if i == 1:
            break

    # todo: 저장 전 순서 바꿔주기
    # todo: 저장하기

    break

