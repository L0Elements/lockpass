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
# kivy
import kivy

kivy.require('2.2.0')
from kivy.app import App
# local library
from ui.Book_view import *
from ui.Password_view import *
from kivy.lang.builder import Builder


class MyApp(App):
    title = "Lockpass 0.0.1"

    #    self.icon = "icon.png"   #App icon
    def build(self):
        self.root = root_book_view()


if __name__ == '__main__':
    MyApp().run()
