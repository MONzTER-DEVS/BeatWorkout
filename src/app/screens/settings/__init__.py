from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen


class SettingsScreen(MDScreen):
    pass


Builder.load_file("app/screens/settings/settings.kv")
