# drop_down_multiplier.py.py
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

@Gtk.Template(resource_path='/com/oyajun/ColorCode/drop_down_multiplier.ui')
class DropDownMultiplier(Gtk.DropDown):
    __gtype_name__ = 'DropDownMultiplier'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        list_store_expression = Gtk.PropertyExpression.new(
            KeyValuePair,
            None,
            'value',
        )

        multiplier_model = Gio.ListStore(item_type=KeyValuePair)
        multiplier_model.splice(
            0, 0,
            [
                KeyValuePair(key='0', value=_('⬛ Black')),
                KeyValuePair(key='1', value=_('🟫 Brown')),
                KeyValuePair(key='2', value=_('🟥 Red')),
                KeyValuePair(key='3', value=_('🟧 Orange')),
                KeyValuePair(key='4', value=_('🟨 Yellow')),
                KeyValuePair(key='5', value=_('🟩 Green')),
                KeyValuePair(key='6', value=_('🟦 Blue')),
                KeyValuePair(key='7', value=_('🟪 Violet')),
                KeyValuePair(key='8', value=_('🩶 Gray')),
                KeyValuePair(key='9', value=_('⬜ White')),
                KeyValuePair(key='-1', value=_('🥇 Gold')),
                KeyValuePair(key='-2', value=_('🥈 Silver')),
                KeyValuePair(key='-3', value=_('🩷 Pink')),
            ],
        )


        self.set_expression(list_store_expression)

        self.set_model(multiplier_model)
