import xlrd, json, urllib, requests

link = 'https://github.com/DIGITbrain/metadata/releases/download/v0.9.8/Metadata.v0.9.8.xlsx'
file_name, headers = urllib.request.urlretrieve(link)
print (file_name)
workbook = xlrd.open_workbook(file_name)
sheet = workbook.sheet_by_index(1)

col_a = sheet.col_values(1,1)
col_b = sheet.col_values(0,4)

my_dict = {a : b for a, b in zip(col_a, col_b)}

app_json = json.dumps(my_dict, indent = 4)
with open(r'output.json', 'w') as f:
    f.write(app_json)

