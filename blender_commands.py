# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT
# MACROPAD Hotkeys: Blender

from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Blender Commands',
    'order': 1,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xCC5500, 'Search', [Keycode.F3]),
        (0xCC5500, 'Render', [Keycode.F12]),
        (0xCC5500, 'RenderA', [Keycode.CONTROL, Keycode.F12]),
        # 2nd row ----------
        (0xCC5500, 'Vertex', ['1']),
        (0x000040, 'Edge', ['2']),
        (0xCC5500, 'Face', ['3']),
        # 3rd row ----------
        (0xCC5500, 'Gizmos', [Keycode.CONTROL,'`']),
        (0x000040, 'Walk/fly', [Keycode.SHIFT, '`']),
        (0xCC5500, 'adjust', [Keycode.F9]),
        # 4th row ----------
        (0xCC5500, 'Open', [Keycode.CONTROL, 'o']),
        (0xCC5500, 'Save', [Keycode.CONTROL, 's']),
        (0xCC5500, 'New', [Keycode.CONTROL, 'n'])
    ]
}
