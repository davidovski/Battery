import random

import HardcodedSettings


def glitch_color(color, amount):
    if HardcodedSettings.GLITCH:
        c = [color[0], color[1], color[2]]
        if random.randint(0,int(100 / amount/10)) == 0:

            v = random.randint(-amount * 64, amount * 64)
            c[0] = (color[0] + v) % 256
            c[1] = (color[1] + v) % 256
            c[2] = (color[2] + v) % 256

        return c
    else:
        return color

def glitch():
    if HardcodedSettings.GLITCH:
        m = 1000
        return random.randint(0, m) == 0
    else:
        return False