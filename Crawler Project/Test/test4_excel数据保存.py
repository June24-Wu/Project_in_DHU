import xlwt
workbook = xlwt.Workbook(encoding='utf-8')   # 创建workbook
worksheet = workbook.add_sheet('sheet1')  # 创建工作表
for i in range(9):
    worksheet.write(0,i,str(i+1))
for i in range(1,9):
    worksheet.write(i,0,str(i+1))
# for i in range(10):
#     for t in range(10):
#         worksheet.write(i,t,str(i*t))

workbook.save('student.xls')
