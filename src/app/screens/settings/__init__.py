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


class SettingsScreen(MDScreen):
    def on_enter(self, *args):
        self.app = MDApp.get_running_app()

    def show_theme_picker(self):
        self.theme_dialog = MDThemePicker()
        self.theme_dialog.open()

    def show_transition_dialog(self):
        self.transition_dialog = MDDialog(
            size_hint=(0.8, 0.5),
            title="Change Transition",
            type="custom",
            content_cls=TransitionContent(),
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
        self.transition_dialog.open()

    def close_dialog(self, *args):
        self.transition_dialog.dismiss()

    def set_transition(self, widget, *args):
        self.transition_content = (
            widget.parent.parent.children[0].parent.parent.children[2].children[0]
        )
        for list_item in self.transition_content.children:
            for check in list_item.children:
                for checkbox in check.children:
                    if str(type(checkbox)) == "<class 'app.screens.settings.RightCheckbox'>":
                        if checkbox.active:
                            pass

        # print(layout.children)
        # for check in layout.children:
        # print(check.active)
        # print(check.children[0].active)
        # if check.active == True:
        # print(check)


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
