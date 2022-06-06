# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT
# MACROPAD Hotkeys: Blender

from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Blender Edit Mode',
    'order': 1,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0A3B66, 'Vertex', [Keycode.ONE]),
        (0x663F00, 'Edge', [Keycode.TWO]),
        (0x0A3B66, 'Face', [Keycode.THREE]),
        # 2nd row ----------
        (0x663F00, 'Separate', [Keycode.P]),
        (0x660556, ' Merge', [Keycode.M]),
        (0x663F00, 'Fill ', [Keycode.F]),
        # 3rd row ----------
        (0x0A3B66, 'Bevel', [Keycode.CONTROL, Keycode.B]),
        (0x663F00, 'VBevel', [Keycode.CONTROL, Keycode.SHIFT, Keycode.B]),
        (0x0A3B66, 'Cancel', [Keycode.ESCAPE]),
        # 4th row ----------
        (0x660556, 'LoopC', [Keycode.CONTROL, Keycode.R]),
        (0x20660A, 'Inset', [Keycode.I]),
        (0x20660A, 'Extrude', [Keycode.E]),
        # Encoder button ---
        (0x000000, '', [Keycode.KEYPAD_PERIOD])
    ]
}

