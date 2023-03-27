import jinja2
import pandas as pd
from ruamel.yaml import YAML
from re import sub

def snake_case(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()

yaml = YAML(typ="safe")


OUTPUT_DIR = "tools/output/user_defs"
excel = "metadata.xlsx"
sheets = pd.read_excel(excel, sheet_name=None)

ASSETS = ("microservice", "algorithm", "model", "data", "ma_pair")

for sheet_name in sheets.keys():
    sheet = pd.read_excel(excel, sheet_name=sheet_name, skiprows=[0], usecols="A:G")

    sheet_list = {}
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
            continue
        # Discard NaN in example values and comments
        example = example if example == example else None

        # Replace <br> tags in examples with line breaks
        try:
            example = example.replace("<br>", "\n            ")
        except AttributeError:
            pass

        comment = comment if comment == comment else "No description available."

        # # Store fields data
        # sheet_list[snake_case(field)] = {
        #         #"required": required,
        #         #"description": comment,
        #         "type": field_type,
        #         "example": example,
        #     }
        if ".md)" in field_type or sheet_name.lower().replace(" ", "_") not in ASSETS:
            sheet_list.setdefault(snake_case(field), {})["type"] = field_type

        if example:
            sheet_list.setdefault(snake_case(field), {})["example"] = example

        if sheet_name.lower().replace(" ", "_") not in ASSETS:
            sheet_list.setdefault(snake_case(field), {})["description"] = comment
        
        
    

    file_name = sheet_name.lower().replace(" ", "_")
    write_path = (
        f"{OUTPUT_DIR}/{file_name}.yaml"
    )
    with open(write_path, "w") as file:
        yaml.default_flow_style = False
        yaml.dump(sheet_list, file)
