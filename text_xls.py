import xlsxwriter

import openpyxl
xl_filename="Files/TradeDairy.xlsx"

book = openpyxl.load_workbook(xl_filename)
rows = (
("ACC1","4/16/2019",1687,1711.5,1703,1681.25,1620,1679.85,1420.3,1723.4,1326),
("ACC2","4/16/2019",1698,1711.5,1703,1681.25,1620,1679.85,1420.3,1723.4,1326)
)

sheet = book['Data']
for row in rows:
    sheet.append(row)
book.save("Files/test.xlsx")


