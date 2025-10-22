# page_5_bands.py
#
# Copyright 2025 oyajun
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

from gi.repository import Adw, Gtk, Gdk, Gio
import decimal
from .utils import *
from .drop_down_value import DropDownValue
from .drop_down_multiplier import DropDownMultiplier
from .drop_down_tolerance import DropDownTolerance

@Gtk.Template(resource_path='/com/oyajun/ColorCode/page_5_bands.ui')
class Page5Bands(Gtk.Box):
    __gtype_name__ = 'Page5Bands'

    drop_down_1 = Gtk.Template.Child()
    drop_down_2 = Gtk.Template.Child()
    drop_down_3 = Gtk.Template.Child()
    drop_down_4 = Gtk.Template.Child()
    drop_down_5 = Gtk.Template.Child()

    result_label = Gtk.Template.Child()

    copy_button = Gtk.Template.Child()

    clipboard = Gdk.Display.get_default().get_clipboard()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.drop_down_1.connect('notify::selected-item', self.on_selected_item)
        self.drop_down_2.connect('notify::selected-item', self.on_selected_item)
        self.drop_down_3.connect('notify::selected-item', self.on_selected_item)
        self.drop_down_4.connect('notify::selected-item', self.on_selected_item)
        self.drop_down_5.connect('notify::selected-item', self.on_selected_item)

        # init
        self.drop_down_1.set_selected(1)
        self.drop_down_2.set_selected(0)
        self.drop_down_3.set_selected(6)
        self.drop_down_4.set_selected(2)
        self.drop_down_5.set_selected(6)


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
        value3 = decimal.Decimal(self.drop_down_3.get_selected_item().key)
        multiplier = decimal.Decimal(self.drop_down_4.get_selected_item().key)
        tolerance = self.drop_down_5.get_selected_item().key

        value = (value1*100 + value2*10 + value3) * decimal.Decimal('10') ** multiplier
        print(value)
        print(convert_to_MKG(value))
        # × U+00D7
        value_str = f'{value1*100 + value2*10 + value3} × 10^{multiplier}Ω ±{tolerance}%'
        print(value_str)
        value_display = f'{convert_to_MKG(value)}Ω ±{tolerance}%'
        self.result_label.set_label(str = value_display)

