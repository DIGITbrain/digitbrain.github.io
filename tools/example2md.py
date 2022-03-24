import pandas as pd
import glob

hide_edits = """
<style>
  .md-content__button {
    display: none;
  }
</style>\n
"""

for example in glob.glob("examples/*.xlsx"):

    sheets = pd.read_excel(example, sheet_name=None)
    file_content = hide_edits
    write_path = "docs/examples/" + example.split("/")[-1].split(".")[0] + ".md"
    for tab in sheets.keys():
        sheet = pd.read_excel(example, sheet_name=tab, skiprows=[0], usecols="A,B,C,H")
        file_content += "\n" + f"# {tab}" + "\n\n"
        sheet.fillna("", inplace=True)
        sheet.replace('\n',' ', regex=True, inplace=True)
        table = sheet.to_markdown(index=False)
        file_content += table + "\n"

    with open(write_path, "w") as file:
        file.write(file_content)