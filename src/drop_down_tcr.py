# drop_down_tcr.py
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


@Gtk.Template(resource_path='/com/oyajun/ColorCode/drop_down_tcr.ui')
class DropDownTcr(Gtk.DropDown):
    __gtype_name__ = 'DropDownTcr'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        list_store_expression = Gtk.PropertyExpression.new(
            KeyValuePair,
            None,
            'value',
        )

        value_model = Gio.ListStore(item_type=KeyValuePair)
        value_model.splice(
            0, 0,
            [
                KeyValuePair(key='250', value=EMOJI_BLACK),
                KeyValuePair(key='100', value=EMOJI_BROWN),
                KeyValuePair(key='50', value=EMOJI_RED),
                KeyValuePair(key='15', value=EMOJI_ORANGE),
                KeyValuePair(key='25', value=EMOJI_YELLOW),
                KeyValuePair(key='20', value=EMOJI_GREEN),
                KeyValuePair(key='10', value=EMOJI_BLUE),
                KeyValuePair(key='5', value=EMOJI_VIOLET),
                KeyValuePair(key='1', value=EMOJI_GRAY),
            ],
        )

        self.set_expression(list_store_expression)

        self.set_model(value_model)
