import sublime, sublime_plugin, os

class CompileLessOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):

        if not view.file_name().endswith('.less'):
            return

        folder_name, file_name = os.path.split(view.file_name()) 
        args = []
        if os.name == "nt":
            args = [sublime.packages_path() + '\lessc\windows\lessc.exe', file_name]
        else:
            args = ['lessc', file_name]             

        view.window().run_command('exec', {'cmd': args, 'working_dir': folder_name})