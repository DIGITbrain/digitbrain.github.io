import pandas, json

file_name = "metadata.xlsx"
workbook = pandas.read_excel(file_name, sheet_name=None)

col_a = sheet.col_values(1)
col_b = sheet.col_values(4)

my_dict = {a : b for a, b in zip(col_a, col_b)}

app_json = json.dumps(my_dict, indent = 4)
with open(r'output.json', 'w') as f:
    f.write(app_json)

