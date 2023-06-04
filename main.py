"""
Copyright (C) 2023 L0Elements

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
# local library
from Lockpass import *
# kivy
import kivy

kivy.require('2.2.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class root(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        main = books()
        self.add_widget(main)


class books(BoxLayout):
    def change_view(self, book):
        pass


    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        b_index = lockpass.booklist()
        if len(b_index) == 0:
            pass
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
                    books.change_view(books, self.usedbook)

            first_layout.add_widget(New_Button())
            del New_Button
            # bt.bind(on_press=self.change_view(item))
            bookindex.add_widget(first_layout)
        scroll.add_widget(bookindex)
        self.add_widget(scroll)


class MyApp(App):
    title = "Lockpass 0.0.1"

    #    self.icon = "icon.png"   #App icon
    def build(self):
        return root()


if __name__ == '__main__':
    MyApp().run()
