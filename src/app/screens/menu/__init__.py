## kivymd
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList, OneLineIconListItem
from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp


## kivy
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

## others
import os, sys


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class MainMenu(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        icons_item = {
            "settings": "Settings",
        }
        for icon_name in icons_item.keys():
            self.ids.md_list.add_widget(
                ItemDrawer(
                    icon=icon_name,
                    text=icons_item[icon_name],
                    on_press=lambda x: MDApp.get_running_app().switch_screen(
                        "settings"
                    ),
                )
            )

    def open_drawer(self):
        self.ids.nav_drawer.set_state("open")


class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """
        Called when tap on a menu item.
        To basically select the item :))
        """

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class MainWidget(MDGridLayout):
    pass


Builder.load_file("app/screens/menu/menu.kv")
