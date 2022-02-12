import jinja2
import pandas as pd

SPECS_DIR = "docs/attributes"
excel = "metadata.xlsx"
sheets = pd.read_excel(excel, sheet_name=None)

for sheet_name in sheets.keys():
    sheet = pd.read_excel(
        excel, sheet_name=sheet_name, skiprows=[0], usecols="A:G"
    )

    sheet_list = []
    for i, subkey in enumerate(sheet["Subkey"]):

        # Use a subkey if there is one, if NaN then skip this cell
        subkey = subkey if all([subkey, subkey == subkey]) else None
        field = subkey if subkey else sheet["Key"][i]
        if isinstance(field, float):
            sheet_list.append({"concept": sheet["Concept"][i]})
            continue

        # Discard NaN in example values and comments
        example = sheet["Example Value"][i]
        example = example if example == example else None

        # Replace <br> tags in examples with line breaks
        try:
            example = example.replace("<br>", "\n            ")
        except AttributeError:
            pass

        comment = sheet["Comment"][i]
        comment = (
            comment if comment == comment else "No description available."
        )

        # Store fields data
        sheet_list.append(
            {
                "concept": None,
                "key": field,
                "required": sheet["Condition"][i],
                "comment": comment,
                "type": sheet["Type"][i],
                "example": example,
                "issubkey": subkey,
            }
        )

    # Fill the template
    jinja_loader = jinja2.FileSystemLoader(searchpath="tools/jinja_templates")
    jinja_env = jinja2.Environment(loader=jinja_loader)
    template = jinja_env.get_template("docspage.md.j2")
    rendered = template.render(sheet_name=sheet_name, fields=sheet_list)
    file_name = sheet_name.lower().replace(" ", "_")
    with open(f"{SPECS_DIR}/{file_name}.md", "w") as file:
        file.write(rendered)
