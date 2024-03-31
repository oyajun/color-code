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

from gi.repository import Adw, Gtk, Gdk, Gio, GObject
import decimal

@Gtk.Template(resource_path='/com/oyajun/ColorCode/window.ui')
class ColorCodeWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ColorCodeWindow'

    drop_down_1 = Gtk.Template.Child()
    drop_down_2 = Gtk.Template.Child()
    drop_down_3 = Gtk.Template.Child()
    drop_down_4 = Gtk.Template.Child()

    result_label = Gtk.Template.Child()

    copy_button = Gtk.Template.Child()

    clipboard = Gdk.Display.get_default().get_clipboard()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        list_store_expression = Gtk.PropertyExpression.new(
            KeyValuePair,
            None,
            "value",
        )

        value_model = Gio.ListStore(item_type=KeyValuePair)
        value_model.splice(
            0, 0,
            [
                KeyValuePair(key="0", value="⬛ Black"),
                KeyValuePair(key="1", value="🟫 Brown"),
                KeyValuePair(key="2", value="🟥 Red"),
                KeyValuePair(key="3", value="🟧 Orange"),
                KeyValuePair(key="4", value="🟨 Yellow"),
                KeyValuePair(key="5", value="🟩 Green"),
                KeyValuePair(key="6", value="🟦 Blue"),
                KeyValuePair(key="7", value="🟪 Violet"),
                KeyValuePair(key="8", value="🩶 Gray"),
                KeyValuePair(key="9", value="⬜ White"),
            ],
        )

        multiplier_model = Gio.ListStore(item_type=KeyValuePair)
        multiplier_model.splice(
            0, 0,
            [
                KeyValuePair(key="0", value="⬛ Black"),
                KeyValuePair(key="1", value="🟫 Brown"),
                KeyValuePair(key="2", value="🟥 Red"),
                KeyValuePair(key="3", value="🟧 Orange"),
                KeyValuePair(key="4", value="🟨 Yellow"),
                KeyValuePair(key="5", value="🟩 Green"),
                KeyValuePair(key="6", value="🟦 Blue"),
                KeyValuePair(key="7", value="🟪 Violet"),
                KeyValuePair(key="8", value="🩶 Gray"),
                KeyValuePair(key="9", value="⬜ White"),
                KeyValuePair(key="-1", value="🥇 Gold"),
                KeyValuePair(key="-2", value="🥈 Silver"),
                KeyValuePair(key="-3", value="🩷 Pink"),
            ],
        )

        tolerance_model = Gio.ListStore(item_type=KeyValuePair)
        tolerance_model.splice(
            0, 0,
            [
                KeyValuePair(key="1", value="🟫 Brown"),
                KeyValuePair(key="2", value="🟥 Red"),
                KeyValuePair(key="0.05", value="🟧 Orange"),
                KeyValuePair(key="0.5", value="🟩 Green"),
                KeyValuePair(key="0.25", value="🟦 Blue"),
                KeyValuePair(key="0.1", value="🟪 Violet"),
                KeyValuePair(key="5", value="🥇 Gold"),
                KeyValuePair(key="10", value="🥈 Silver"),
            ],
        )

        self.drop_down_1.set_expression(list_store_expression)
        self.drop_down_2.set_expression(list_store_expression)
        self.drop_down_3.set_expression(list_store_expression)
        self.drop_down_4.set_expression(list_store_expression)

        self.drop_down_1.set_model(value_model)
        self.drop_down_2.set_model(value_model)
        self.drop_down_3.set_model(multiplier_model)
        self.drop_down_4.set_model(tolerance_model)

        self.drop_down_1.connect("notify::selected-item", self.on_selected_item)
        self.drop_down_2.connect("notify::selected-item", self.on_selected_item)
        self.drop_down_3.connect("notify::selected-item", self.on_selected_item)
        self.drop_down_4.connect("notify::selected-item", self.on_selected_item)

        # init
        self.drop_down_1.set_selected(1)
        self.drop_down_2.set_selected(0)
        self.drop_down_3.set_selected(2)
        self.drop_down_4.set_selected(6)

        self.calculate()

        self.copy_button.connect('clicked', self.copy_text)

    def copy_text(self, _button):
        self.clipboard.set(self.result_label.get_label())

    def on_selected_item(self, _drop_down, _selected_item):
        selected_item = _drop_down.get_selected_item()
        self.calculate()

    def calculate(self):
        value1 = decimal.Decimal(self.drop_down_1.get_selected_item().key)
        value2 = decimal.Decimal(self.drop_down_2.get_selected_item().key)
        multiplier = decimal.Decimal(self.drop_down_3.get_selected_item().key)
        tolerance = self.drop_down_4.get_selected_item().key

        value = (value1*10 + value2) * decimal.Decimal("10") ** multiplier
        print(value)
        print(convert_to_MKG(value))
        # × U+00D7
        value_str = f"{value1*10 + value2} × 10^{multiplier}Ω ±{tolerance}%"
        print(value_str)
        value_display = f"{convert_to_MKG(value)}Ω ±{tolerance}%"
        self.result_label.set_label(str = value_display)

def convert_to_MKG(value):
    if value < 1000:
        return delete_zero(value)
    elif value < 1000000:
        return delete_zero(value/1000) + "K"
    elif value < 1000000000:
        return delete_zero(value/1000000) + "M"
    elif value < 1000000000000:
        return delete_zero(value/1000000000) + "G"

def delete_zero(value):
    if value % decimal.Decimal("1") == 0:   # the value has .0
        return str(int(value))
    elif value % decimal.Decimal("0.1") == 0:
        return str(value.quantize(decimal.Decimal('1.0')))
    elif value % decimal.Decimal("0.01") == 0:
        return str(value.quantize(decimal.Decimal('1.00')))
    elif value % decimal.Decimal("0.001") == 0:
        return str(value.quantize(decimal.Decimal('1.000')))
    else:
        return str(value)

class KeyValuePair(GObject.Object):
    key = GObject.Property(
        type=str,
        flags=GObject.ParamFlags.READWRITE,
    )
    value = GObject.Property(
        type=str,
        nick="Value",
        blurb="Value",
        flags=GObject.ParamFlags.READWRITE,
        default="",
    )

