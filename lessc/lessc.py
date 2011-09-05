import sublime, sublime_plugin, subprocess, os

class CompileLessOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):

        if not view.file_name().endswith('.less'):
            return

        if os.name == "nt":
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        folder_name, file_name = os.path.split(view.file_name())
        args = [sublime.packages_path() + '\lessc\windows\lessc.exe', '-m', file_name]        
        view.window().run_command('exec', {'cmd': args, 'working_dir': folder_name})
        process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, startupinfo=startupinfo)