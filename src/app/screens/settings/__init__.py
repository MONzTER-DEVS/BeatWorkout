from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.app import MDApp
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.properties import StringProperty


class SettingsScreen(MDScreen):
    def on_enter(self, *args):
        self.app = MDApp.get_running_app()

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def show_transition_dialog(self):
        self.transition_dialog = MDDialog(
            size_hint=(0.8, 0.5),
            title="Change Transition",
            type="custom",
            content_cls=TransitionContent(),
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.app.theme_cls.primary_color
                ),
                MDFlatButton(text="APPLY", text_color=self.app.theme_cls.primary_color),
            ],
        )
        self.transition_dialog.open()

    def on_leave(self, *args):
        self.app.theme_data["preference1"] = {"theme": self.app.theme_cls.theme_style}
        self.app.theme_data["preference2"] = {
            "color": self.app.theme_cls.primary_palette
        }


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    """Custom list item."""

    slide_icon = StringProperty("android")


class TransitionContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.adaptive_height = True


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    """Custom right container."""


Builder.load_file("app/screens/settings/settings.kv")
