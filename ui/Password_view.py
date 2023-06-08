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
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Pwd_head(BoxLayout):
    upper = ''

    def __init__(self):
        super().__init__()
        self.size_hint_y = .26
        self.add_widget(Label(text=self.upper.book, font_size='40sp', bold=True, underline=True,
                              size_hint_x=.65))  # Name of the book


class Pwd_body(BoxLayout):
    upper = ''
    pass


class PasswordView(BoxLayout):
    book = ""
    upper = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.upper = self
        Pwd_head.upper = self.upper
        Pwd_body.upper = self.upper

        self.orientation = 'vertical'

        self.add_widget(Pwd_head())
        self.add_widget(Pwd_body())
