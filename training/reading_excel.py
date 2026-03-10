'''


'''

import xlrd

xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True

path = r'C:\Users\Ramya\PycharmProjects\selenium_KIIT\files\candidates_kiit.xlsx'

## open the excel
workbook = xlrd.open_workbook(path)
# print(workbook)             ## book object

## open the worksheet
worksheet = workbook.sheet_by_name("Sheet1")
# print(worksheet)            ## sheet object

## convert the sheet object to the generator object
rows = worksheet.get_rows()
# print(rows)

##----------------------------------------------------------------

# for ele in rows:
#     print(ele)
#
# ## [text:'name', text:'place', text:'phone_num']
# ## [text:'Adithya', text:'Bhuvaneshwar', number:9874563210.0]
# ## [text:'Siddarth', text:'Himachal Pradesh', number:9685741230.0]
# ## [text:'Himanshi', text:'Raipur', number:8974563212.0]
# ## [text:'Suraj', text:'Odissa', number:8963250147.0]

##----------------------------------------------------------------
#
# for ele in rows:
#     print(ele[0], ele[1], ele[2])
#
# ## text:'name' text:'place' text:'phone_num'
# ## text:'Adithya' text:'Bhuvaneshwar' number:9874563210.0
# ## text:'Siddarth' text:'Himachal Pradesh' number:9685741230.0
# ## text:'Himanshi' text:'Raipur' number:8974563212.0
# ## text:'Suraj' text:'Odissa' number:8963250147.0


##----------------------------------------------------------------

for ele in rows:
    print(ele[0].value, ele[1].value, ele[2].value)
































































