from gmap_direction import GmapDirection, result2dict
from openpyxl import Workbook

from tools import excel_to_dict, is_excel
import os

key = os.environ.get('SJANG_GOOGLEAPI')
gmap = GmapDirection(key=key)

in_dirname = './straight/'
straight = os.listdir(in_dirname)

num_find = 3

for f in straight:
    if not is_excel(f):
        continue

    fname = os.path.join(in_dirname, f)
    print('input:', fname)
    out_name = 'gmap_direction_' + str(fname).split('_')[-1]
    print('output:', out_name)

    wb = Workbook()
    ws = wb.active

    offices = excel_to_dict(fname, mute=True)

    len_offices = len(offices)
    for i, office in enumerate(offices):
        origin = (office['Y'], office['X'])
        for num in range(num_find):
            destination = (office['Y_hosp' + str(num + 1)], office['X_hosp' + str(num + 1)])
            direction_result = gmap.get_direction(origin, destination)
            direction_dict = result2dict(direction_result, num + 1)
            office.update(direction_dict)

        # Add header in the first row
        if i == 0:
            ws.append(list(office.keys()))

        ws.append(list(office.values()))
        if (i + 1) % 50 == 0 or i + 1 == len_offices:
            print('find offices [{}/{}]'.format(i + 1, len_offices))
            wb.save(out_name)

    wb.save(out_name)
    print('saved to :', out_name)

print('\n-----done-----\n')
