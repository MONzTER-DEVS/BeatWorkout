from kivy.lang.builder import Builder
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem, ILeftBodyTouch
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.picker import MDThemePicker


class SettingsScreen(MDScreen):

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()


Builder.load_file("app/screens/settings/settings.kv")
