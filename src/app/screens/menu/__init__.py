from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.boxlayout import BoxLayout
import os, sys


class MainMenu(MDScreen):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class MainWidget(MDGridLayout):
    pass


Builder.load_file("app/screens/menu/menu.kv")
