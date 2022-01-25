import pandas, json, ast, sys


def to_json(file_name):
    workbook = pandas.read_excel(file_name, sheet_name=None)

    my_dict = {}

    for sheet_name in workbook:
        # Load each sheet
        sheet = pandas.read_excel(
            file_name, sheet_name=sheet_name, skiprows=[0], usecols="B,C,D,G,H"
        )

        # Top-level JSON key for each sheet
        my_dict.setdefault(sheet_name, {})

        # Parent key for nested subkeys
        parent_key = ""

        # Iterate over rows in required columns
        for i, (key, subkey, value, field_type, required) in enumerate(
            zip(
                sheet["Key"],
                sheet["Subkey"],
                sheet["Values"],
                sheet["Type"],
                sheet["Condition"],
            )
        ):

            # skip row if type cell is empty (assume rest of row is too)
            if isinstance(field_type, float):
                continue

            # Eval / clean value
            try:
                value = ast.literal_eval(value)
            except (ValueError, SyntaxError):
                value = value if all([value, value == value]) else None

            # Clean/assign required, subkey and key
            subkey = subkey if all([subkey, subkey == subkey]) else None
            required = required if all([required, required == required]) else ""
            key = key if all([key, key == key, not subkey]) else parent_key

            # Get the next subkey along
            try:
                next_subkey = sheet["Subkey"][i + 1]
            except KeyError:
                next_subkey = None
            next_subkey = (
                next_subkey if all([next_subkey, next_subkey == next_subkey]) else None
            )

            # Creating objects
            if not subkey and next_subkey is not None:
                parent_key = key
                if "list" in field_type.lower() or "array" in field_type.lower():
                    my_dict[sheet_name].setdefault(key, []).append({})
                elif "map" in field_type.lower():
                    my_dict[sheet_name].setdefault(key, {})

            # Normal behaviour - only keys
            elif not subkey:
                if not value and "mandatory" not in required.lower():
                    continue
                my_dict[sheet_name][key] = value

            # Nesting key-values pairs in objects
            else:
                if not value and "mandatory" not in required.lower():
                    continue
                try:
                    my_dict[sheet_name][key].setdefault(subkey, value)
                except AttributeError:
                    my_dict[sheet_name][key][0][subkey] = value
    return my_dict

if __name__ == "__main__":
    # Quick filename as arg
    if len(sys.argv) == 1:
        file = "metadata.xlsx"
        path = "tools/output/output.json"
    else:
        if not sys.argv[1].endswith(".xlsx"):
            print("Not a .xlsx file!")
            sys.exit(1)
        file = sys.argv[1]
        path = f"{file[-15:-5]}.json"

    metadata = to_json(file)
    
    # dump the JSON
    app_json = json.dumps(metadata, indent=4)
    with open(path, "w") as f:
        f.write(app_json)
