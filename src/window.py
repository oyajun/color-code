# window.py
#
# Copyright 2024 jun
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw, Gtk, Gio, GObject

@Gtk.Template(resource_path='/com/oyajun/ColorCode/window.ui')
class ColorCodeWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ColorCodeWindow'

    test_drop = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        list_store_expression = Gtk.PropertyExpression.new(
                KeyValuePair,
                None,
                "value",
        )


        model = Gio.ListStore(item_type=KeyValuePair)
        model.splice(
            0, 0,
            [
                KeyValuePair(key=0, value="⬛ Black"),
                KeyValuePair(key=1, value="🟫 Brown"),
                KeyValuePair(key=2, value="🟥 Red"),
                KeyValuePair(key=3, value="🟧 Orange"),
                KeyValuePair(key=4, value="🟨 Yellow"),
                KeyValuePair(key=5, value="🟩 Green"),
                KeyValuePair(key=6, value="🟦 Blue"),
                KeyValuePair(key=7, value="🟪 Violet"),
                KeyValuePair(key=8, value="👽 Gray"),
                KeyValuePair(key=9, value="⬜ White"),
            ],
        )

        list_store_expression = Gtk.PropertyExpression.new(
            KeyValuePair,
            None,
            "value",
        )

        self.test_drop.set_expression(list_store_expression)
        self.test_drop.set_model(model)

        self.test_drop.connect("notify::selected-item", self.on_advanced_selected_item)

    def on_advanced_selected_item(self, _drop_down, _selected_item):
        selected_item = _drop_down.get_selected_item()
        if selected_item:
            print(selected_item.key)

class KeyValuePair(GObject.Object):
    key = GObject.Property(
        type=int,
        flags=GObject.ParamFlags.READWRITE,
    )
    value = GObject.Property(
        type=str,
        nick="Value",
        blurb="Value",
        flags=GObject.ParamFlags.READWRITE,
        default="",
    )
