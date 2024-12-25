from openpyxl import Workbook
from openpyxl.styles import Font

# Creating a new Excel workbook and sheet
wb = Workbook()
ws = wb.active

# Automate data entry
data = [
    ['Name', 'Age'],
    ['John', 28],
    ['Anna', 24],
    ['Peter', 35],
    ['Linda', 32]
]

for row in data:
    ws.append(row)

# Automate formatting
for cell in ws["1:1"]:
    cell.font = Font(bold=True)

# Saving the workbook
wb.save('automated_task.xlsx')