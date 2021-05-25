from app.screens import menu, settings
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
from kivy.properties import ColorProperty, NumericProperty, StringProperty
import os, sys

Window.size = (480, 800)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(base_path, relative_path)


resource_add_path(resource_path(os.path.join("app", "screens", "menu")))
resource_add_path(resource_path(os.path.join("app", "screens", "settings")))
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


class BeatWorkoutApp(MDApp):
    theme = StringProperty("Dark")
    transition = StringProperty("Slide")
    text_color = ColorProperty([0, 0, 0, 1])
    bg_color = ColorProperty([66 / 255, 66 / 255, 66 / 255, 1])


    def build(self):
        self.theme_cls.primary_palette = "Lime"
        self.theme_cls.theme_style = "Dark"  # "Light"
        self.root = ScreenManager()
        self.menu = menu.MainMenu()
        self.settings = settings.SettingsScreen()
        self.screens = {"menu": self.menu, "settings": self.settings}
        self.root.switch_to(self.menu)
        return self.root

    def switch_screen(self, screen, direction="left"):
        self.root.transition.direction = direction
        self.root.switch_to(self.screens[screen])


if __name__ == "__main__":
    BeatWorkoutApp().run()
