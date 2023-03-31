import sys
from pathlib import Path

import jinja2
import requests
from ruamel.yaml import YAML, scanner

yaml = YAML(typ="safe")

jinja_loader = jinja2.FileSystemLoader(searchpath="tools/jinja_templates")
jinja_env = jinja2.Environment(loader=jinja_loader)
template = jinja_env.get_template("docspage.md.j2")

API_BASE_URL = "https://dbs-api.emgora.eu/v1/emgamr/api/"
UDT_LIST_URL_PATH = "udt_list"

CUSTOM_DEFS_PATH = Path("docs/custom_definitions")
FIELDS_DIR = Path("docs/attributes")

AMDR_TABLES = (
    "microservice",
    "algorithm",
    "model",
    "data",
    "ma_pair",
)
DA_TABLES = ("dma_tuple",)  # Need the comma for a tuple
DA_UDTS = ("deployment",)


## General
errors = []
pages_to_write = []


def fetch_api_detail(url, key=None):
    try:
        response = requests.get(url)
    except requests.RequestException as e:
        raise ValueError(f"ERR: Could not connect to {url}: {e}.") from None

    if response.status_code != 200:
        raise ValueError(f"ERR: Could not find spec at {url}: {response}.")

    try:
        return response.json()[key] if key else response.json()
    except KeyError:
        raise ValueError(f"ERR: JSON does not contain {key}: {response}.") from None


def notify_missing_info(table, field, field_def):
    notice = f"::notice file=docs/custom_definitons/{table}.yaml::{field}"
    if table not in DA_TABLES and "example" not in field_def:
        msg = "is missing an example value."
        print(f"{notice} {msg}")

    if table not in DA_TABLES and table not in AMDR_TABLES:
        if "description" not in field_def:
            msg = "is missing a description."
            print(f"{notice} {msg}")


def update_fields_with_user_defs(table, fields, user_defs):
    if not fields:  # For tables not in AMDR, rely on user definitions
        return user_defs

    table = table.lower().replace(" ", "_")
    msg = "does not have a custom definition so may be missing info."

    for field, defs in fields.items():
        if field not in user_defs:
            print(f"::notice file=docs/custom_definitons/{table}.yaml::{field} {msg}")
            continue

        defs.update(user_defs[field])
        notify_missing_info(table, field, fields[field])

    return fields


def get_user_definitions(table):
    try:
        return yaml.load(CUSTOM_DEFS_PATH / f"{table}.yaml")

    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"WARN: No user definitions found for {table} table."
        ) from None

    except scanner.ScannerError as e:
        raise ValueError(
            f"ERR: Failed parsing user definitions for {table} table: {e}."
        ) from None


## Asset Stuff
definitions = fetch_api_detail(API_BASE_URL, "definitions")

for table in AMDR_TABLES + DA_TABLES + DA_UDTS:
    fields = {}
    user_defs = {}
    try:
        if table in AMDR_TABLES:
            fields = definitions[table]["properties"]
            required = definitions[table]["required"]
        user_defs = get_user_definitions(table)

    except KeyError:
        errors.append(f"ERR: No API definitions found for {table}.")
        continue

    except ValueError as error:
        errors.append(error)
        continue

    except FileNotFoundError:
        if table in DA_TABLES:
            errors.append(f"ERR: Expecting user definitions for {table}, none found.")
            continue

    fields = update_fields_with_user_defs(table, fields, user_defs)

    pages_to_write.append(
        {
            "table": table.title(),
            "fields": fields,
            "required": required,
            "asset": table in AMDR_TABLES,
        }
    )


## UDT Helper Functions
def clean_udts(udts):
    cleaned_udts = {}
    for udt in udts:
        udt_name = udt.pop("udt_name")
        udt_field_name = udt.pop("udt_field_name")
        udt["type"] = udt.pop("udt_field_data_type").replace(
            "character varying", "string"
        )

        cleaned_udts.setdefault(udt_name, {})[udt_field_name] = udt
    return cleaned_udts


## UDT Stuff
udts = fetch_api_detail(API_BASE_URL + "udt_list")
udts = clean_udts(udts)
for udt, fields in udts.items():
    if len(fields) <= 2:
        continue

    user_defs = {}
    try:
        user_defs = get_user_definitions(udt)
    except Exception:
        pass

    fields = update_fields_with_user_defs(udt, fields, user_defs)

    pages_to_write.append(
        {
            "table": udt.title(),
            "fields": fields,
            "required": {},
            "asset": False,
        }
    )

## Render & write pages
for page_data in pages_to_write:
    rendered = template.render(**page_data)
    file_name = page_data["table"].lower().replace(" ", "_")

    write_path = (
        FIELDS_DIR / f"{file_name}/index.md"
        if file_name in AMDR_TABLES + DA_TABLES
        else FIELDS_DIR / f"{file_name}.md"
    )
    with open(write_path, "w") as file:
        file.write(rendered)


if errors:
    [print(error) for error in errors]
    sys.exit(1)
