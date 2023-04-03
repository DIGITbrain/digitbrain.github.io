# Contributing

Thanks for your interest in contributing to the DIGITbrain documentation.

There are several parts to the documentation, please see the relevant section
below for information on how to contribute.

## How to Contribute

We welcome changes to the documentaion via Pull Requests. If you're not comfortable
working with git/GitHub, please [open an issue](https://github.com/DIGITbrain/digitbrain.github.io/issues/new) instead.

Pull Requests will be automatically checked for basic errors, and will require reviewer approval before merging.

### Rendering Locally

You can render the site locally to preview your changes, using `mkdocs serve`. Make sure you
install the `mkdocs-material` package first.
```bash
pip install mkdocs-material swagger-markdown
mkdocs serve

```

Then find the site at http://127.0.0.1:8000

### Generating Asset Detail

To preview your changes to the **Assets in Detail** pages, run the script at
`tools/postgrest-to-detail.py`. Install the necessary dependencies first.

```bash
pip install -r tools/requirements.txt
python tools/postgrest-to-detail.py

```

## Contributing by Section

Here is some info about how to make contributions to the various sections.

### Home, Getting Started, Going Further

These sections are Markdown rendered to static pages by [mkdocs-material](https://squidfunk.github.io/mkdocs-material/).
Most contributions here will only require some basic familiarity with [Markdown](https://www.markdownguide.org/getting-started/).
Links to these three sections are below:

- [Home](https://github.com/DIGITbrain/digitbrain.github.io/blob/main/docs/index.md)
- [Getting Started](https://github.com/DIGITbrain/digitbrain.github.io/tree/main/docs/start)
- [Going Further](https://github.com/DIGITbrain/digitbrain.github.io/tree/main/docs/adv)


### Asset Overview (table format)

This section is generated using a plugin called [`swagger-markdown`](https://github.com/batiste/swagger-markdown).
A daily GitHub Action keeps the OpenAPI Specification of the Asset Metadata Registry up-to-date
at [tools/swagger.json](https://github.com/DIGITbrain/digitbrain.github.io/blob/main/tools/swagger.json),
and when MkDocs publishes the site, definitions are automatically rendered as tables.

If you wish to propose changes to this section, the templates for asset overviews are
[located in this directory](https://github.com/DIGITbrain/digitbrain.github.io/tree/main/docs/tables).

### Assets in Detail (listing)

This section is generated using a Python script at
[tools/postgrest-to-detail.py](https://github.com/DIGITbrain/digitbrain.github.io/blob/main/tools/postgrest-to-detail.py).
The script calls the Asset Metadata Registry (AMR) API to pull the latest definitions and UDTs. It then renders the asset detail
pages using this [Jinja2 template](https://github.com/DIGITbrain/digitbrain.github.io/blob/main/tools/jinja_templates/docspage.md.j2).

To document other (future) assets or substructures, follow these steps:

#### For substructures in the AMR (UDTs)

- Substructures in the AMR `udt_list` will have pages automatically generated for them
- Just [run the script](#generating-asset-detail)
- And add the entry (normally `attributes/<substructure_name>.md`) to the [navigation](#modifying-the-navigation)

#### For assets in the AMR

- Add the Asset name to [AMDR_TABLES](https://github.com/DIGITbrain/digitbrain.github.io/blob/bad026a265034608b90cd875482479e0c1430638/tools/postgrest-to-detail.py#L20) in `postgrest-to-detail.py`
- Then [run the script](#generating-asset-detail) and add the entry (normally `attributes/<asset_name>.md`) to the [navigation](#modifying-the-navigation)

#### For assets/substructures not in the AMR

- First add the Asset name to [DA_TABLES (assets)](https://github.com/DIGITbrain/digitbrain.github.io/blob/bad026a265034608b90cd875482479e0c1430638/tools/postgrest-to-detail.py#L27) or [DA_UDTS (substructures)](https://github.com/DIGITbrain/digitbrain.github.io/blob/bad026a265034608b90cd875482479e0c1430638/tools/postgrest-to-detail.py#L28)
- Then create a [Custom Definitions](#customising-details) file at [`custom_definitions/<name>.yaml`](https://github.com/DIGITbrain/digitbrain.github.io/tree/main/docs/custom_definitions)
- Finally [run the script](#generating-asset-detail) and add the entry to the [navigation](#modifying-the-navigation)

## Further Info

### Modifying the Navigation

Re-ordering or otherwise modifying the navigation of the site is possible by editing
the [`nav`](https://github.com/DIGITbrain/digitbrain.github.io/blob/bad026a265034608b90cd875482479e0c1430638/mkdocs.yml#L19)
key in `mkdocs.yml`. You can add new assets or substructures to the
[Assets Overview (tables)](https://github.com/DIGITbrain/digitbrain.github.io/blob/bad026a265034608b90cd875482479e0c1430638/mkdocs.yml#L55)
or [Assets in Detail](https://github.com/DIGITbrain/digitbrain.github.io/blob/bad026a265034608b90cd875482479e0c1430638/mkdocs.yml#L33)
sections of the file, just point to the location of the newly generated `.md` file.

### Customising Details

Customisations to asset or substructure fields are supported via these
[YAML files](https://github.com/DIGITbrain/digitbrain.github.io/tree/main/docs/custom_definitions).
Via these files, you can overwrite the type, description, optionality and examples of assets
and substructures in the AMR.

> Note you cannot add new fields to assets or substructures in the AMR. These should instead be
> added to the AMR and picked up via automation.

You can also use these files to create detail listings for assets or substructures that do
[not appear in the AMR](#for-assetssubstructures-not-in-the-amr).

Let's look at a truncated copy of `deployment.yaml` to see how we can create or overwrite a listing:

```yaml
id:
  hide: true
type:
  required: true
  description: |
    DIGITbrain supports cloud infrastructure deployed via ...
  example: cloudbroker
  type: Enumeration ["cloudbroker", "edge"]

Cloudbroker:
  header: true

deployment_id:
  description: |
    A CloudBroker deployment ties together software...
  example:
    MiCADO-Optimised: 1860cb3f-4f23-417f-a1f1-3705158cd3b3
    Ubuntu 20.04: 16b1e2d4-3a2c-406e-8c45-5637099021f0
    Ubuntu 18.04: 5a081b54-8992-4ff7-8a21-74e425062507
  type: string (UUID)
  required: true
```

Notes:
- Top-level keys are the names of fields for this asset or substructure
- Fields can be hidden with `hide: true` (e.g. for fields auto-filled by the DA)
- Optionality is by default `optional` but can be overwritten with `required: true`
- Description supports multi-line YAML
- When example is a string, a single example is created in a code block
- When example is a map, multiple examples are created in a [tabbed](https://facelessuser.github.io/pymdown-extensions/extensions/tabbed/) code block
- Headers at ### level can be created with `header: true` in this case, the key is the header text
- Types can be overwritten
- This order of fields will only be preserved for structures **NOT** in the AMR

## Maintainer Notes

- A release will trigger the GitHub workflow to publish the site
- Pull requests will only trigger the linting action
- Commits to main will trigger the generate action, which may auto-commit
  - The auto-commit message will re-use the message of the latest
    commit in the series of pushed/merged commits
- Examples are no longer generated from Excel sheets
  - We should probably re-think how we present these