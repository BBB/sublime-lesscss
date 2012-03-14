import sublime, sublime_plugin, os
from lessc_opts import lessc_opts

class CompileLessOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):

        if not view.file_name().endswith('.less'):
            return

        folder_name, file_name = os.path.split(view.file_name()) 

        args = []
        path = ''

        out_file_name = file_name.replace('.less', '.css')
        
        if os.name == "nt":
            args = [sublime.packages_path() + '\lessc\windows\lessc.exe']
            if lessc_opts['min']:
                args.append('-m')
            args.append(view.file_name())
        else:
            args = ['lessc', file_name]
            path = '/usr/local/bin'
            if lessc_opts['min']:
                args.append('-x')

        view.window().run_command('exec', {'cmd': args, 'working_dir': folder_name, 'path':path })

        if lessc_opts['use_tabs']:
            openfile = open(os.path.join(folder_name, out_file_name), 'r+w')
            css = openfile.read()
            css = css.replace('  ', '\t')
            openfile.write(css)
            openfile.close()