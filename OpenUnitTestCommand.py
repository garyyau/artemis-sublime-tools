import os
import sublime_plugin


class JavaScriptFile():
    """
    JavaScript File object, storing locational information about the fiel based on
    the absolute path.
    """

    def __init__(self, file_path):
        """
        Constructor

        Takes the file_path and breaks it down into the different locational
        information components.
        """
        location, file_name = os.path.split(file_path)
        base_name, ext = os.path.splitext(file_name)

        self.path = file_path
        self.location = location
        self.base_name = base_name
        self.ext = ext

    @staticmethod
    def create(file_path):
        """
        Creates a JavaScript File object based on the file_path. Also ensures that
        the file exists on the system, or else it will create it.
        """
        file = JavaScriptFile(file_path)
        path = file.get_path()
        location = file.get_location()

        if not os.path.exists(location):
            os.makedirs(location)
        open(path, "a")

        return file

    def get_path(self):
        return self.path

    def get_location(self):
        return self.location

    def get_base_name(self):
        return self.base_name

    def get_ext(self):
        return self.ext


class OpenJasmineUnitTest(sublime_plugin.TextCommand):
    """
    Command to open a Jasmine Unit Test spec file based on the current
    target JavaScript file.
    """

    def run(self, edit):
        self.load_project_paths()

        current_file_path = self.view.file_name()
        current_file = JavaScriptFile(current_file_path)

        spec_path = self.get_spec_path(current_file)
        spec_file = JavaScriptFile.create(spec_path)

        self.view.window().open_file(spec_file.get_path())

    def load_project_paths(self):
        """
        Loads the `project_paths` parameters from the Sublime Text project settings
        file, looking for the `jasmine_spec` location and `javascript_src` location.
        """
        paths = self.view.window().project_data().get("project_paths", {})
        self.spec_location = paths["jasmine_spec"]
        self.src_location = paths["javascript_src"]

    def get_spec_path(self, current_file):
        """
        Gets the path that the spec file should exist in based on the path
        of the current file.
        """
        spec_dir = self.get_spec_location(current_file)
        spec_file_name = self.get_spec_file_name(current_file)
        return spec_dir + "\\" + spec_file_name

    def get_spec_location(self, file):
        """
        Gets the location that the spec file should exist in based on the location
        of the current file.
        """
        file_location = file.get_location()
        if not file_location.startswith(self.src_location):
            return
        return file_location.replace(
            self.src_location,
            self.spec_location
        )

    def get_spec_file_name(self, file):
        """
        Gets the spec file name based on the name of the current file.
        """
        file_base_name = file.get_base_name()
        file_ext = file.get_ext()
        return file_base_name + "_spec" + file_ext
