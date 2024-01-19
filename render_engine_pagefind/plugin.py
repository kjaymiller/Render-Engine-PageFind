import subprocess
from render_engine.plugins import hook_impl


class PageFind:
    @hook_impl
    def post_build_site(site):
        if subprocess.check_output(["npx", "-y", "pagefind", "--site", site.output_path]):
            print("PageFind ran successfully")
        else:
            raise InterruptedError("PageFind failed to run")