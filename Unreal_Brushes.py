# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MITS
# MACROPAD Hotkeys: Unreal

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Unreal Brushes', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x202000, 'Sel', [Keycode.SHIFT, '1']),
        (0x202000, 'Land', [Keycode.SHIFT, '2']),
        (0x202000, 'Foli', [Keycode.SHIFT, '3']),
        # 2nd row ----------
        (0x202000, 'Mesh', [Keycode.SHIFT, '4']),
        (0x202000, 'Model', [Keycode.SHIFT, '5']),
        (0x202000, 'Frac', [Keycode.SHIFT, '6']),
        # 3rd row ----------
        (0x202000, 'Br ED', [Keycode.SHIFT, '7']),
        (0x202000, 'Ani', [Keycode.SHIFT, '8']),
        (0x202000, '3', ['3']),
        # 4th row ----------
        (0x101010, '*', ['*']),
        (0x800000, '0', ['0']),
        (0x101010, '#', ['#']),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
