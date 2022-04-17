import subprocess

import sublime
import sublime_plugin


class BlackFormat(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        subprocess.check_call("black '%s'" % view.file_name(), shell=True)
