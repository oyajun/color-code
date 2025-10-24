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
                KeyValuePair(key='250', value=_('⬛ Black')),
                KeyValuePair(key='100', value=_('🟫 Brown')),
                KeyValuePair(key='50', value=_('🟥 Red')),
                KeyValuePair(key='15', value=_('🟧 Orange')),
                KeyValuePair(key='25', value=_('🟨 Yellow')),
                KeyValuePair(key='20', value=_('🟩 Green')),
                KeyValuePair(key='10', value=_('🟦 Blue')),
                KeyValuePair(key='5', value=_('🟪 Violet')),
                KeyValuePair(key='1', value=_('🩶 Gray')),
            ],
        )

        self.set_expression(list_store_expression)

        self.set_model(value_model)
