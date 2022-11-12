import xlrd
import numpy as np
import json
def extract(file,index=3):
    workbook = xlrd.open_workbook(file)
    worksheet = workbook.sheet_by_index(index)
    rows = worksheet.nrows
    c = tuple(worksheet.row_values(i)[:] for i in range(rows))

    return c




