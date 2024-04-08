"""Eon Collective Documentation theme"""

import os
from importlib.metadata import version
from sphinx.config import Config

__version__ = version("eon_collective_docs_theme")
__version_full__ = __version__


def get_html_theme_path():
    """Return absolute path to parent folder of installed theme."""
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def update_context(app, pagename, templatename, context, doctree):
    """Update the rendering context for a page.

    This function makes the theme version available in the Jinja2 html
    templates as `{{ theme_version }}`.

    Additionally we tweak the rendering context in an unconventional way. We
    are inspecting the context to see whether the page meta data has an entry
    `template`. If so, we expect the value of that entry to be the name of a
    template file that should be used for rendering instead of the default
    template `page.html`.

    A field field list near the top of a reST source file is passed on by
    Sphinx as file metadata. For example, a line `:template: sitemap.html'
    right at the beginning of a reST file will tell Sphinx to use the template
    file `sitemap.html` for this page instead of the default template file
    `page.html`.

    """
    context["theme_version"] = __version__
    parent_dir = os.path.dirname(os.path.dirname(__file__))
    docs_dir = os.path.join(parent_dir, "docs")
    config_file_path = docs_dir
    if os.path.isdir(os.path.join(docs_dir, "source")):
        config_file_path = os.path.join(docs_dir,"source")

    config_values = Config.read(confdir=config_file_path)._raw_config
    if(config_values.get("repository")):
        context["repository"] = config_values["repository"]
    return app.builder.env.metadata.get(pagename, {}).get("template")

def setup(app):
    """Setup functionality called by Sphinx"""
    app.connect("html-page-context", update_context)
    if hasattr(app, "add_html_theme"):
        theme_path = os.path.abspath(os.path.dirname(__file__))
        app.add_html_theme("eon_collective_docs_theme", theme_path)
    # unconfirmed: just assuming that parallel_write_safe is ok
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
