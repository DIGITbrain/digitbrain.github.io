import pandas as pd


excel = "metadata.xlsx"
sheets = pd.read_excel(excel, sheet_name=None)
hide_edits = """
<style>
  .md-content__button {
    display: none;
  }
</style>\n
"""

ASSETS = ("microservice", "algorithm", "model", "data", "ma_pair", "dma_tuple")

for tab in sheets.keys():
    sheet = pd.read_excel(excel, sheet_name=tab, skiprows=[0], usecols="A:G")
    sheet_name = tab.lower().replace(" ", "_")
    sheet.fillna("", inplace=True)
    table = sheet.to_markdown(index=False)
    details_link = (
        "**This information is also available in** "
        f"**[list format](/attributes/{sheet_name}/)**\n\n"
    )

    write_path = (
        f"docs/tables/{sheet_name}/index.md"
        if sheet_name in ASSETS
        else f"docs/tables/{sheet_name}.md"
    )
    with open(write_path, "w") as file:
        file.write(hide_edits + details_link + table)
    print(f"Converted to {sheet_name}.md...")
