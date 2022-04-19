import subprocess

import sublime_plugin


class BlackFormat(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        if view.file_name().endswith(".py"):
            subprocess.run(f"black {view.file_name()}".split(), shell=True)
