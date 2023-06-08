from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
class param():
    book = ''
class view(BoxLayout):
    def __init__(self):
        super().__init__()
        self.add_widget(Label(text=param.book))
class Password_viewApp(App):
    def build(self):
        return Label(text="hello World!")