import xlrd

path = r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\ddt\reg_testdata.xlsx'


def excel_data():
    workbook = xlrd.open_workbook(path)             ## Book object
    worksheet = workbook.sheet_by_name("reg")       ## sheet object
    rows = worksheet.get_rows()                     ## generator object
    header = next(rows)

    d = {}
    for ele in rows:
        d[ele[0].value] = ele[1].value
    return d















































































