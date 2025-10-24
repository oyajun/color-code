# drop_down_tolerance.py
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

from gi.repository import Gtk, Gio
from .utils import KeyValuePair
from .colors import *


@Gtk.Template(resource_path='/com/oyajun/ColorCode/drop_down_tolerance.ui')
class DropDownTolerance(Gtk.DropDown):
    __gtype_name__ = 'DropDownTolerance'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        list_store_expression = Gtk.PropertyExpression.new(
            KeyValuePair,
            None,
            'value',
        )

        tolerance_model = Gio.ListStore(item_type=KeyValuePair)
        tolerance_model.splice(
            0, 0,
            [
                KeyValuePair(key='1', value=EMOJI_BROWN),
                KeyValuePair(key='2', value=EMOJI_RED),
                KeyValuePair(key='0.05', value=EMOJI_ORANGE),
                KeyValuePair(key='0.5', value=EMOJI_GREEN),
                KeyValuePair(key='0.25', value=EMOJI_BLUE),
                KeyValuePair(key='0.1', value=EMOJI_VIOLET),
                KeyValuePair(key='5', value=EMOJI_GOLD),
                KeyValuePair(key='10', value=EMOJI_SILVER),
            ],
        )

        self.set_expression(list_store_expression)

        self.set_model(tolerance_model)
