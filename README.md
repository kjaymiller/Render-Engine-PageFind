# PageFind

PageFind theme and plugin that adds page find to your site.

## How to use this theme

1. Install the theme

   ```python
   pip install render_engine_pagefind
   ```

2. Import the theme into your project

   ```python
   from render_engine import Site
   from render_engine_pagefind import PageFind

   app = Site()
   app.register_theme(PageFind)
   ```
