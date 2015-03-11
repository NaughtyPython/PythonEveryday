import os
import path
import xlsxwriter
stu_path = os.path.abspath(os.path.join(path.assets_path, 'student.txt'))
workbook = xlsxwriter.Workbook(os.path.abspath(os.path.join(path.assets_path, 'demo.xlsx')))
worksheet = workbook.add_worksheet()


with open(stu_path) as f:
    s = f.read()
    import ast
    dict = ast.literal_eval(s)
    row = 0
    for key in dict.keys():
        row = row + 1
        worksheet.write('A%s' % row, key)
    row_item = 0
    for key, item in dict.items():
        row_item = row_item + 1
        column = 97
        for i in item:
            column = column + 1
            worksheet.write('%s%s' % (chr(column).upper(), row_item), str(i).decode('utf-8'))

    workbook.close()

