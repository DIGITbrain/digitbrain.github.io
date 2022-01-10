import pandas as pd

excel = "metadata.xlsx"
sheets = pd.read_excel(excel, sheet_name=None)

for sheet_name in sheets.keys():
    sheet = pd.read_excel(excel, sheet_name=sheet_name, skiprows=[0], usecols="A:G")
    sheet_name = sheet_name.lower().replace(" ", "_")
    sheet.to_csv(f"assets/{sheet_name}.csv", index=False)    
    print(f"Generating {sheet_name}.csv...")
