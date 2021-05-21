from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.gridlayout import MDGridLayout

from kivy.graphics import Rectangle
from kivy.graphics.texture import Texture

from kivy.core.window import Window
Window.size = (480, 800)

class GradientBack(Widget):
    def __init__(self, **args):
        # super(GradientBack, self).__init__(**args)

        # self.texture = Texture.create(size=(2, 1), colorfmt='rgb')

        # color1 = 0
        # color2 = 255

        # buf = int(map(chr, [color1, color2]))

        # self.texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

        # with self.canvas:
        #     Rectangle(pos=self.pos, size=self.size, texture=self.texture)
        pass

class MainWidget(MDGridLayout):
    pass


class BeatWorkoutApp(MDApp):
    # def build(self):
    #     return GradientBack(size=(200, 200))
    pass


BeatWorkoutApp().run()