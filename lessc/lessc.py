import sublime
import sublime_plugin
import os
from lessc_opts import lessc_opts


class CompileLessOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):

        if not view.file_name().endswith('.less'):
            return

        folder_name, file_name = os.path.split(view.file_name())

        args = []
        path = ''

        out_file_name = file_name.replace('.less', '.css')
        out_path = os.path.join(folder_name, out_file_name)

        if os.name == "nt":
            args = [sublime.packages_path() + '\lessc\windows\lessc.exe']
            if lessc_opts['min']:
                args.append('-m')
            args.append(view.file_name())

        else:
            args = ['lessc', view.file_name()]
            path = '/usr/local/bin'
            if lessc_opts['min']:
                args.append('-x')

        if lessc_opts['split_folders']:
            if folder_name[-4:] == 'less':
                folder_path, css_folder_name = os.path.split(folder_name)
                folder_path = os.path.join(folder_path, 'css')
                if not os.path.isdir(folder_path):
                    os.mkdir(folder_path)
                out_path = os.path.join(folder_path, out_file_name)
                args.append(out_path)

        view.window().run_command('exec', {'cmd': args, 'working_dir': folder_name, 'path': path})
