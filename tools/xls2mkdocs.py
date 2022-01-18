import jinja2
import pandas as pd

SPECS_DIR = "docs/attributes"
excel = "metadata.xlsx"
sheets = pd.read_excel(excel, sheet_name=None)

for sheet_name in sheets.keys():
    sheet = pd.read_excel(
        excel, sheet_name=sheet_name, skiprows=[0], usecols="A:G"
    )

    sheet_dictionary = {}
    for i, subkey in enumerate(sheet["Subkey"]):

        # Use a subkey if there is one, if NaN then skip this cell
        field = subkey if subkey == subkey else sheet["Key"][i]
        if isinstance(field, float):
            sheet_dictionary[sheet["Concept"][i]] = None
            continue

        # Store fields data
        sheet_dictionary[field] = (
            sheet["Condition"][i],
            sheet["Comment"][i],
            sheet["Type"][i],
            sheet["Example Value"][i],
        )

    # Fill the template
    jinja_loader = jinja2.FileSystemLoader(searchpath="tools/jinja_templates")
    jinja_env = jinja2.Environment(loader=jinja_loader)
    template = jinja_env.get_template("docspage.md.j2")
    rendered = template.render(sheet_name=sheet_name, fields=sheet_dictionary)
    file_name = sheet_name.lower().replace(" ", "_")
    with open(f"{SPECS_DIR}/{file_name}.md", "w") as file:
        file.write(rendered)
