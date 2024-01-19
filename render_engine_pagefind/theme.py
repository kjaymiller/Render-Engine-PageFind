import pathlib

from jinja2 import DictLoader
from render_engine.themes import Theme

from .plugin import PageFind as PageFindPlugin

# Add plugins here
templates = {"pagefind.html": """{% macro pagefind() %}
<link href="/pagefind/pagefind-ui.css" rel="stylesheet">
<script src="/pagefind/pagefind-ui.js"></script>
<div id="search"></div>
<script>
    window.addEventListener('DOMContentLoaded', (event) => {
        new PagefindUI({ element: "#search", showSubResults: true });
    });
</script>
{% endmacro %}}"""}

pagefind = Theme(
    loader = DictLoader(templates),
    prefix = "pagefind",
    static_dir= pathlib.Path(__file__).parent / "static",
    plugins = [PageFindPlugin],
    filters = {},
)