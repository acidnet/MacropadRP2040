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
        (0XCC5500, 'Vertex', [Keycode.ONE]),
        (0xCC5500, 'Edge', [Keycode.TWO]),
        (0xCC5500, 'Face', [Keycode.THREE]),
        # 2nd row ----------
        (0xCC5500, 'Separate', [Keycode.P]),
        (0x000040, ' Merge', [Keycode.M]),
        (0xCC5500, 'Fill ', [Keycode.F]),
        # 3rd row ----------
        (0xCC5500, 'Bevel', [Keycode.CONTROL, Keycode.B]),
        (0x000040, 'VBevel', [Keycode.CONTROL, Keycode.SHIFT, Keycode.B]),
        (0xCC5500, 'Cancel', [Keycode.ESCAPE]),
        # 4th row ----------
        (0xCC5500, 'LoopC', [Keycode.CONTROL, Keycode.R]),
        (0xCC5500, 'Inset', [Keycode.I]),
        (0xCC5500, 'Extrude', [Keycode.E]),
        # Encoder button ---
        (0x000000, '', [Keycode.KEYPAD_PERIOD])
    ]
}

