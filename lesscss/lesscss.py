# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import os


class LessCss(sublime_plugin.EventListener):

    def on_post_save(self, view):

        if not view.file_name().endswith('.less'):
            return

        s = sublime.load_settings('LessCss.sublime-settings')
        LessCss.minify = s.get('minify', False)
        LessCss.split_folders = s.get('split_folders', False)

        folder_name, file_name = os.path.split(view.file_name())

        args = []
        path = ''

        out_file_name = file_name.replace('.less', '.css')
        out_path = os.path.join(folder_name, out_file_name)

        if os.name == 'nt':
            args = [sublime.packages_path() + '\lesscss\windows\lessc.exe']
            if LessCss.minify:
                args.append('-m')
            args.append(view.file_name())
        else:

            args = ['lessc', view.file_name()]
            path = '/usr/local/bin'
            if LessCss.minify:
                args.append('-x')

        if LessCss.split_folders:
            if folder_name[-4:] == 'less':
                folder_path, css_folder_name = os.path.split(folder_name)
                folder_path = os.path.join(folder_path, 'css')
                if not os.path.isdir(folder_path):
                    os.mkdir(folder_path)
                out_path = os.path.join(folder_path, out_file_name)
        args.append(out_path)

        view.window().run_command('exec', {'cmd': args, 'working_dir': folder_name, 'path': path})
