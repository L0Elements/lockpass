# local library
from local.Lockpass import *
# kivy
import kivy

kivy.require('2.2.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class root(BoxLayout):
    pass


class MyApp(App):
    title = "Lockpass 0.0.1"

    #    self.icon = "icon.png"   #App icon
    def build(self):
        return root()


if __name__ == '__main__':
    MyApp().run()
