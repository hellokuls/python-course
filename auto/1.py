# 导入第三方库
import xlrd
# 读取Python进击者.xlsx文件
a = xlrd.open_workbook('Python进击者.xlsx')

all_sheets = a.sheets()

for sheet in all_sheets:
    rows = sheet.nrows
    cols = sheet.ncols
    for row in range(0, rows):
        for col in range(0, cols):
            print(sheet.cell_value(row, col))
