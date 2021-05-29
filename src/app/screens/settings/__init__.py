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
from kivy.metrics import dp
from kivy.clock import Clock
import webbrowser

class SettingsScreen(MDScreen):
    def on_enter(self, *args):
        self.app = MDApp.get_running_app()

    def show_theme_picker(self):
        self.theme_dialog = MDThemePicker()
        self.theme_dialog.open()

    def show_transition_dialog(self):
        self.transition_content = TransitionContent()
        self.transition_dialog = MDDialog(
            size_hint=(0.8, 0.5),
            title="Change Transition",
            type="custom",
            content_cls=self.transition_content,
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    text_color=self.app.theme_cls.primary_color,
                    on_release=self.close_dialog,
                ),
                MDFlatButton(
                    text="APPLY",
                    text_color=self.app.theme_cls.primary_color,
                    on_release=self.set_transition,
                ),
            ],
        )
        self.check_current_transition()
        self.transition_dialog.open()

    def check_current_transition(self, *args):
        for list_item in self.transition_content.children:
            if list_item.text == self.app.transition:
                list_item.children[0].children[0].active = True

    def close_dialog(self, *args):
        self.transition_dialog.dismiss()

    def checked(self, widget, *args):
        self.seleced_transition = widget.parent.parent.text

    def set_transition(self, widget, *args):
        self.transition_dialog.dismiss()
        Clock.schedule_once(
            lambda x: self.app.change_transition(self.seleced_transition)
        )

    def rate(self, *args):
        """
        will lead to the play store page of your app
        """
        webbrowser.open(self.app.rate)


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    pass


class TransitionContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.adaptive_height = True


class Check(MDCheckbox):
    pass


class RightCheckbox(IRightBodyTouch, Check):
    pass


Builder.load_file("app/screens/settings/settings.kv")
