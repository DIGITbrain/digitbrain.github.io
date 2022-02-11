import pandas as pd


excel = "metadata.xlsx"
sheets = pd.read_excel(excel, sheet_name=None)

prepend = """
<style>
  .md-typeset h1,
  .md-content__button {
    display: none;
  }
</style>"""

for sheet_name in sheets.keys():
    sheet = pd.read_excel(
        excel, sheet_name=sheet_name, skiprows=[0], usecols="A:G"
    )
    sheet_name = sheet_name.lower().replace(" ", "_")
    sheet.fillna("", inplace=True)
    table = sheet.to_markdown(index=False)
    with open(f"docs/tables/{sheet_name}.md", "w") as file:
        file.write(prepend + "\n" + table)
    print(f"Converted to {sheet_name}.md...")
