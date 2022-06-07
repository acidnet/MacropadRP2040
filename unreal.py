# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Unreal

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Unreal Viewport', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x2596be, 'Trans', ['W']),
        (0x2596be, 'Rot', ['E']),
        (0x2596be, 'Scl', ['R']),
        # 2nd row ----------
        (0x2596be, 'FS', [Keycode.F11]),
        (0x2596be, 'Focus', ['F']),
        (0x2596be, 'Space', [Keycode.CONTROL, '`']),
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
