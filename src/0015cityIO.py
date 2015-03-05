#coding=utf-8
import os
import path

city = {
        "1":"北京",
        "2":"成都"
        }
city_path = os.path.abspath(os.path.join(path.assets_path, 'city.txt'))

with open(city_path, 'w') as f:
    f.write(str(city))
    f.close()

with open(city_path, 'r') as f:
    s = f.read()
    import ast
    d = ast.literal_eval(s)
    print d
    import xlsxwriter
    workbook = xlsxwriter.Workbook(os.path.abspath(os.path.join(path.assets_path,'city.xlsx')))
    worksheet = workbook.add_worksheet('sheet2')
    for key in d:
        worksheet.write('A%s' % key, key)
        worksheet.write('B%s' % key, d[key].decode('utf-8'))
    workbook.close()


import xlrd
wb = xlrd.open_workbook(os.path.abspath(os.path.join(path.assets_path,'city.xlsx')))
sheet = wb.sheet_by_index(0)


xml_version = "<?xmlversion=1.0 encoding='UTF-8'?>"
result = xml_version
for row in range(0, sheet.nrows):
    values = sheet.row_values(row)
    print "values %s %s" % (values[0], values[1])
    tag = values[0]
    content = values[1]
    result = result + '\n' + tag + ':' +  content
print result

with open(os.path.abspath(os.path.join(path.assets_path, 'result.xml')), 'w') as f:
    f.write(result.encode('utf-8'))
f.close()