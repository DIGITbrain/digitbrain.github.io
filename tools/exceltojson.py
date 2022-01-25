import xlrd, json

file_name = "metadata.xlsx"
workbook = xlrd.open_workbook(file_name)
sheet = workbook.sheet_by_index(1)

col_a = sheet.col_values(1)
col_b = sheet.col_values(4)

my_dict = {a : b for a, b in zip(col_a, col_b)}

app_json = json.dumps(my_dict, indent = 4)
with open(r'output.json', 'w') as f:
    f.write(app_json)

