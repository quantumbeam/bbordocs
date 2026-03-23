# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'bbordocs'
# copyright = '2026, suzuki'
author = 'ks'
release = 'n'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

root_doc = 'index'
extensions = [
    "sphinx.ext.autosectionlabel",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_context = {
    "languages": [
        ("ja", "/ja/"),
        ("en", "/en/"),
    ]
}
html_theme_options = {
    "navbar_end": ["theme-switcher", "version-switcher"],

    "switcher": {
        "json_url": "_static/switcher.json",
        "version_match": "ja",  # JAビルド時に上書きする
    },
}