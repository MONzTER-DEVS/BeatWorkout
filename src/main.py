from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.gridlayout import MDGridLayout
from kivy.graphics import Rectangle
from kivy.graphics.texture import Texture
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.resources import resource_add_path
from kivymd.uix.list import MDList, OneLineIconListItem
from kivy.properties import StringProperty
import os, sys

Window.size = (480, 800)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(base_path, relative_path)


resource_add_path(resource_path(os.path.join("app", "screens", "menu")))
resource_add_path(resource_path(os.path.join("fonts", "Roboto_Condensed")))


# class GradientBack(Widget):
#     def __init__(self, **args):
#         # super(GradientBack, self).__init__(**args)

#         # self.texture = Texture.create(size=(2, 1), colorfmt='rgb')

#         # color1 = 0
#         # color2 = 255

#         # buf = int(map(chr, [color1, color2]))

#         # self.texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

#         # with self.canvas:
#         #     Rectangle(pos=self.pos, size=self.size, texture=self.texture)
#         pass

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()

class BeatWorkoutApp(MDApp):

    def open_drawer(self):
        self.menu.ids.nav_drawer.set_state("open")

    def build(self):
        self.theme_cls.primary_palette = 'DeepOrange'
        self.theme_cls.theme_style = "Dark"  # "Light"

        # if getattr(sys, "frozen", False):
        from app.screens import (
            menu,
        )
        self.root = ScreenManager()
        self.menu = menu.MainMenu()
        self.screens = {"menu": self.menu}
        self.root.switch_to(self.menu)

        return self.root

    def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }
        for icon_name in icons_item.keys():
            self.menu.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )



if __name__ == "__main__":
    BeatWorkoutApp().run()
