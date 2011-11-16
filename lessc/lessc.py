import sublime, sublime_plugin, os
from lessc_opts import lessc_opts

class CompileLessOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):

        if not view.file_name().endswith('.less'):
            return

        folder_name, file_name = os.path.split(view.file_name()) 
        args = []
        path = ''
        
        if os.name == "nt":
            args = [sublime.packages_path() + '\lessc\windows\lessc.exe']
            if lessc_opts['min']:
                args.append('-m')
        else:
            args = ['lessc', file_name]
            path = '/usr/local/bin'
            if lessc_opts['min']:
                args.append('-x')

        args.append(file_name)

        view.window().run_command('exec', {'cmd': args, 'working_dir': folder_name, 'path':path })