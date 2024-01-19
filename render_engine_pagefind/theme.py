import pathlib

from jinja2 import PackageLoader
from render_engine.utils.themes import Theme

from .plugin import PageFind as PageFindPlugin

# Add plugins here

PageFind = Theme(
    loader=PackageLoader(f"render_engine_pagefind", "templates"),
    static_dir= pathlib.Path(__file__).parent / "static",
    plugins = [PageFindPlugin],
    filters = {},
)