from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from Lockpass import *


class root_book_view(BoxLayout):
    def to_passwd_view(self, book):
        self.clear_widgets()

    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        b_index = lockpass.booklist()
        upper = self
        if len(b_index) == 0:
            pass
        else:
            bookindex = BoxLayout(orientation="vertical")
            scroll = ScrollView(do_scroll_x=False)
            for item in b_index:
                first_layout = BoxLayout(orientation="horizontal", height='120sp')
                second_layout = BoxLayout(orientation="vertical", size_hint=(.8, 1))

                second_layout.add_widget(Label(text=item, font_size='24sp', size_hint_y=.8, halign='left'))
                second_layout.add_widget(Label(text=lockpass.bookinfo.Description(item), size_hint_y=.2, halign='left'))

                first_layout.add_widget(second_layout)

                # btn = Button(text="Open Book", size_hint=(.2, 1))
                # btn.bind(on_press='self.change_view(item)')
                class New_Button(Button):
                    text = "Open Book"
                    size_hint = (.2, 1)
                    usedbook = item

                    def on_press(self):
                        root_book_view.to_passwd_view(upper, self.usedbook)

                first_layout.add_widget(New_Button())
                del New_Button
                # bt.bind(on_press=self.change_view(item))
                bookindex.add_widget(first_layout)
            scroll.add_widget(bookindex)
            self.add_widget(scroll)
