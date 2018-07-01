from openpyxl import load_workbook, Workbook
from haversine import haversine
import heapq
import time


def excel_to_dict(excel_path, headers=[]):
    wb = load_workbook(excel_path)
    sheet = wb.worksheets[0]

    dict_list = []
    total = sheet.max_row
    for i, row in enumerate(sheet.rows):
        row_values = [c.value for idx, c in enumerate(row)]
        if i == 0:
            headers = row_values
        else:
            one_dict = dict(zip(headers, row_values))
            dict_list.append(one_dict)

        if (i + 1) % 100 == 0 or i + 1 == total:
            print('excel to dict: [{}/{}]'.format(i + 1, total))

    return dict_list

