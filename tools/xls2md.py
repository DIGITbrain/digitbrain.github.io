import shutil
import os

import pandas as pd
from mdtable import MDTable


excel = "metadata.xlsx"
sheets = pd.read_excel(excel, sheet_name=None)
os.makedirs("csv", exist_ok=True)

for sheet_name in sheets.keys():
    sheet = pd.read_excel(
        excel, sheet_name=sheet_name, skiprows=[0], usecols="A:G"
    )
    sheet_name = sheet_name.lower().replace(" ", "_")
    sheet.to_csv(f"csv/{sheet_name}.csv", index=False)
    print(f"Generated {sheet_name}.csv...")
    markdown = MDTable(f"csv/{sheet_name}.csv")
    markdown_table = markdown.get_table()
    markdown.save_table(f"docs/tables/{sheet_name}.md")
    print(f"Converted to {sheet_name}.md...")

shutil.rmtree("csv")
print(f"Cleaned up csv files...")
