__version__ = "0.0.1"  # app version
import os, sys, json

os.environ["KIVY_NO_CONSOLELOG"] = "1"

from app.screens import menu, settings
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.gridlayout import MDGridLayout
from kivy.graphics import Rectangle
from kivy.graphics.texture import Texture
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.core.window import Window
from kivy.resources import resource_add_path
from kivymd.uix.list import MDList, OneLineIconListItem
from kivy.properties import ColorProperty, NumericProperty, StringProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import (
    ScreenManager,
    FadeTransition,
    CardTransition,
    NoTransition,
)

# Window.size = (480, 800)


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

    transitions = {
        "Fade": FadeTransition,
        "Card": CardTransition,
        "Slide": SlideTransition,
        "None": NoTransition,
    }

    dirname, filename = os.path.split(os.path.abspath(__file__))
    try:
        content_data = JsonStore(os.path.join("assets/data", "main_content.json"))
        theme_data = JsonStore(os.path.join("assets/data", "preferences.json"))
    except:
        content_data = JsonStore(
            os.path.join("src", "assets/data", "main_content.json")
        )
        theme_data = JsonStore(os.path.join("src", "assets/data", "preferences.json"))

    def build(self):
        self.theme_cls.primary_palette = "Lime"
        self.theme_cls.theme_style = "Dark"  # "Light"
        self.root = ScreenManager()
        self.menu = menu.MainMenu()
        self.settings = settings.SettingsScreen()
        self.screens = {"menu": self.menu, "settings": self.settings}
        self.root.switch_to(self.menu)
        return self.root

    def on_stop(self, *args):
        self.theme_data["preference1"] = {"theme": self.theme_cls.theme_style}
        self.theme_data["preference2"] = {"color": self.theme_cls.primary_palette}
        self.theme_data["preference3"] = {"transition": self.transition}

    def on_start(self):
        theme = self.theme_data["preference1"]["theme"]
        color = self.theme_data["preference2"]["color"]
        transition = self.theme_data["preference3"]["transition"]
        self.theme_cls.theme_style = theme
        self.theme_cls.primary_palette = color
        self.transition = transition
        self.root.transition = self.transitions[transition]()

    def switch_screen(self, screen, direction="left"):
        self.root.transition.direction = direction
        self.root.switch_to(self.screens[screen])

    def change_transition(self, transition, *args):
        self.transition = transition
        self.root.transition = self.transitions[transition]()


if __name__ == "__main__":
    BeatWorkoutApp().run()
