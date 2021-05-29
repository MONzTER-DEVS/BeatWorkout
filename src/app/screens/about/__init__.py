from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import webbrowser


class AboutScreen(MDScreen):
    def source_code(self, *args):
        webbrowser.open(MDApp.get_running_app().source_code)


Builder.load_file("app/screens/about/about.kv")
