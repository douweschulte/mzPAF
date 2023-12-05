"""Configuration file for the Sphinx documentation builder."""

# Scripts
import json
import jsonschema2md

def get_jsonschema_docs(input_json, output_markdown):
    """Generate markdown documentation from a JSON schema."""
    parser = jsonschema2md.Parser()
    with open(input_json, encoding="utf-8") as f_in:
        output_md = parser.parse_schema(json.load(f_in))

    with open(output_markdown, "w", encoding="utf-8") as f_out:
        f_out.writelines(output_md)

get_jsonschema_docs(
    "../specification/annotation-schema.json",
    "../specification/annotation-schema.md"
)


# Project information
project = "mzPAF"
author = "HUPO-PSI"
github_project_url = "https://github.com/HUPO-PSI/mzPAF"
github_doc_root = "https://github.com/HUPO-PSI/mzPAF/tree/master/docs"

# General configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_click.ext",
    "myst_parser",
]
source_suffix = [".rst", ".md"]
master_doc = "index"
exclude_patterns = ["_build"]

# Options for HTML output
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/HUPO-PSI/mzPAF",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        }
    ]
}

# Autodoc options
autodoc_default_options = {"members": True, "show-inheritance": True}
autodoc_member_order = "bysource"
autodoc_typehints = "description"
autoclass_content = "init"

# Intersphinx options
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "psims": ("https://mobiusklein.github.io/psims/docs/build/html/", None),
    "pyteomics": ("https://pyteomics.readthedocs.io/en/stable/", None),
}


def setup(app):
    config = {"enable_eval_rst": True}  # noqa: F841

