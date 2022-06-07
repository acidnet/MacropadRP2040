# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT
# MACROPAD Hotkeys: Unreal

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Unreal Files', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x33f30a, 'New', [Keycode.CONTROL, 'N']),
        (0x33f30a, 'Open', [Keycode.CONTROL, 'O']),
        (0x33f30a, 'Save', [Keycode.CONTROL, 'S']),
        # 2nd row ----------
        (0x33f30a, 'Save as', [Keycode.CONTROL, Keycode.ALT, 'S']),
        (0x33f30a, '', ['']),
        (0x33f30a, 'Save all', [Keycode.CONTROL, Keycode.SHIFT, 'S']),
        # 3rd row ----------
        (0x202000, '1', ['1']),
        (0x202000, '2', ['2']),
        (0x202000, '3', ['3']),
        # 4th row ----------
        (0x101010, '*', ['*']),
        (0x800000, '0', ['0']),
        (0x101010, '#', ['#']),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
