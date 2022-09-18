from os.path import isfile

from xlrd import open_workbook


def get_rows(file="../whatsapp.xlsx"):
    if not file or not isfile(file):
        print(f'{file} is not a valid path')
        exit(-1)
    try:
        wb = open_workbook(file)
    except Exception as e:
        print(f'{file} is not a valid file')
        exit(-1)
        raise e
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    for row in sheet.get_rows():
        try:
            yield int(row[0].value), row[1].value
        except Exception as e:
            print(f'Failed to parse row {row}, {e}')
