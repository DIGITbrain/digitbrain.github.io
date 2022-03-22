import jinja2
import pandas as pd

SPECS_DIR = "docs/attributes"
excel = "metadata.xlsx"
sheets = pd.read_excel(excel, sheet_name=None)

ASSETS = ("microservice", "algorithm", "model", "data", "ma_pair", "dma_tuple")

for sheet_name in sheets.keys():
    sheet = pd.read_excel(excel, sheet_name=sheet_name, skiprows=[0], usecols="A:G")

    sheet_list = []
    for (key, subkey, example, field_type, required, comment, concept) in zip(
        sheet["Key"],
        sheet["Subkey"],
        sheet["Example Value"],
        sheet["Type"],
        sheet["Condition"],
        sheet["Comment"],
        sheet["Concept"],
    ):
        if not any ([key == key, subkey == subkey, concept == concept]):
            continue

        # Use a subkey if there is one, if NaN then skip this cell
        subkey = subkey if all([subkey, subkey == subkey]) else None
        field = subkey if subkey else key
        if isinstance(field, float):
            sheet_list.append({"concept": concept})
            continue

        # Discard NaN in example values and comments
        example = example if example == example else None

        # Replace <br> tags in examples with line breaks
        try:
            example = example.replace("<br>", "\n            ")
        except AttributeError:
            pass

        comment = comment if comment == comment else "No description available."

        # Store fields data
        sheet_list.append(
            {
                "concept": None,
                "key": field,
                "required": required,
                "comment": comment,
                "type": field_type,
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

    write_path = (
        f"{SPECS_DIR}/{file_name}/index.md"
        if file_name in ASSETS
        else f"{SPECS_DIR}/{file_name}.md"
    )
    with open(write_path, "w") as file:
        file.write(rendered)
