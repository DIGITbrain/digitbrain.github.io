import pandas as pd


excel = "metadata.xlsx"
sheets = pd.read_excel(excel, sheet_name=None)
hide_edits = """
<style>
  .md-content__button {
    display: none;
  }
</style>
"""


for tab in sheets.keys():
    sheet = pd.read_excel(excel, sheet_name=tab, skiprows=[0], usecols="A:G")
    sheet_name = tab.lower().replace(" ", "_")
    sheet.fillna("", inplace=True)
    table = sheet.to_markdown(index=False)
    with open(f"docs/tables/{sheet_name}.md", "w") as file:
        file.write(hide_edits + "\n" + table)
    print(f"Converted to {sheet_name}.md...")
