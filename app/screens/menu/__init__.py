from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.gridlayout import MDGridLayout
import os, sys


class MainMenu(MDScreen):
    pass


class MainWidget(MDGridLayout):
    pass


Builder.load_file("menu.kv")
