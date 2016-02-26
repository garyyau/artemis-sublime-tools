import os
import sublime_plugin


class JavaScriptFile():
    def __init__(self, file_path):
        file_location, file_name = os.path.split(file_path)
        base_name, ext = os.path.splitext(file_name)

        self.file_location = file_location
        self.base_name = base_name
        self.ext = ext

    def get_location(self):
        return self.file_location

    def get_base_name(self):
        return self.base_name

    def get_ext(self):
        return self.ext


class OpenJasmineUnitTest(sublime_plugin.TextCommand):
    def run(self, edit):
        self.load_project_paths()

        current_file_path = self.view.file_name()
        current_file = JavaScriptFile(current_file_path)

        spec_path = self.get_spec_path(current_file)

        spec_file_path = self.get_spec_file_path()
        self.view.window().open_file(spec_file_path)

    def load_project_paths(self):
        paths = self.view.window().project_data().get("project_paths", {})
        self.spec_location = paths["jasmine_spec"]
        self.src_location = paths["javascript_src"]

    def get_spec_path(self, current_file):
        spec_dir = self.get_spec_location(current_file)
        spec_file_name = self.get_spec_file_name(current_file)
        return spec_dir + "\\" + spec_file_name

        if not os.path.exists(spec_file_dir):
            os.makedirs(spec_file_dir)

        current_file = self.current_file
        spec_file = (current_file.get_file_name() +
                     "_spec" + current_file.get_file_ext())
        spec_file_path = spec_file_dir + "\\" + spec_file
        open(spec_file_path, "a")
        return spec_file_path

    def get_spec_location(self, file):
        file_location = file.get_location()
        if not file_location.startswith(self.src_location):
            return
        return file_location.replace(
            self.src_location,
            self.spec_location
        )

    def get_spec_file_name(self, file):
        file_base_name = file.get_base_name()
        file_ext = file.get_ext()
        return file_base_name + "_spec" + file_ext
