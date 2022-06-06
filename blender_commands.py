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
        (0x0A3B66, 'Search', [Keycode.F3]),
        (0x663F00, 'Render', [Keycode.F12]),
        (0x000000, 'RenderA', [Keycode.CONTROL, Keycode.F12]),
        # 2nd row ----------
        (0x663F00, 'Vertex', ['1']),
        (0x660556, 'Edge', ['2']),
        (0x663F00, 'Face', ['3']),
        # 3rd row ----------
        (0x0A3B66, 'Gizmos', [Keycode.CONTROL,'`']),
        (0x663F00, 'Walk/fly', [Keycode.SHIFT, '`']),
        (0x0A3B66, 'adjust', [Keycode.F9]),
        # 4th row ----------
        (0x660556, 'Open', [Keycode.CONTROL, 'o']),
        (0x20660A, 'Save', [Keycode.CONTROL, 's']),
        (0x20660A, 'New', [Keycode.CONTROL, 'n'])
    ]
}
