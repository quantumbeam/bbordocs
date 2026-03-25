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

html_title = 'BBO-Rietveld'
html_baseurl = 'https://quantumbeam.github.io/bbordocs/'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_context = {
    "languages": [
        ("ja", "/ja/"),
        ("en", "/en/"),
    ]
}
html_sidebars = {
    '**': [
        'globaltoc.html',
    ],
    'using/windows': [
        'windows-sidebar.html',
        'searchbox.html',
    ],
}
html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": None,
    "navbar_end": ["theme-switcher", "version-switcher"],

    "show_nav_level": 2,
    "navigation_depth": 4,

    "switcher": {
        "json_url": "_static/switcher.json",
        "version_match": "ja",  # JAビルド時に上書きする
    },
}

