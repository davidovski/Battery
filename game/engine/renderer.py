import pygame
import engine.Object

MAX_DEPTH = 64


class PerspectiveRender:
    def __init__(self, surface):
        self.to_draw = []
        self.screen = surface
        self.pers = [-1, -1]

    def add_object(self, object):
        self.to_draw.append(object)

    def add_objects(self, objects):
        for obj in objects:
            self.to_draw.append(obj)

    def set_perspective(self, x, y):
        self.pers = [x, y]

    def change_perspective(self, x, y):
        self.pers[0] += x
        self.pers[1] += y

    def render(self):
        for d in range(0, MAX_DEPTH + 1):
            for o in self.to_draw:
                if o.z < d < o.z + o.depth:
                    offset = [self.pers[0] * (MAX_DEPTH / 2 - d), self.pers[1] * (MAX_DEPTH / 2 - d)]

                    o.draw_cross_section(self.screen, offset)
        self.to_draw[:] = []

