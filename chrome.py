# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys: Chrome

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Chrome', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'win', [Keycode.CONTROL, 'N']),
        (0x002000, 'tab', [Keycode.CONTROL, 'T']),
        (0x800000, 'incog', [Keycode.CONTROL, Keycode.SHIFT, 'N']),
        # 2nd row ----------
        (0x202000, 'Home', [Keycode.ALT, Keycode.HOME]),
        (0x000020, 'CL-tab', [Keycode.CONTROL, 'w']),
        (0x002000, 'CL-win', [Keycode.ALT, Keycode.SHIFT, 'w']),
        # 3rd row ----------
        (0x800000, 'History', [Keycode.CONTROL, 'h']),
        (0x202000, ' DL', [Keycode.CONTROL, 'j']),
        (0x000020, 'Find', [Keycode.CONTROL, 'f']),
        # 4th row ----------
        (0x000040, 'Zoom +', [Keycode.CONTROL, Keycode.KEYPAD_PLUS]),
        (0x800000, 'Zoom -', [Keycode.CONTROL, Keycode.KEYPAD_MINUS]),
        (0x202000, 'Normal', [Keycode.CONTROL, '0']),
        # Encoder button ---
        (0x000000, '', [Keycode.SHIFT, Keycode.ESCAPE])
    ]
}
# Write your code here :-)
