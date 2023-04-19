import random

from engine.Object import Object3D
import pygame

from engine.util import glitch_color, glitch


class Cuboid(Object3D):
    def __init__(self, x, y, z, width, height, depth, color):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.depth = depth
        self.color = color
        self.border = True

    def draw_cross_section(self, surface, offset):
        c = glitch_color(self.color, 1)

        if glitch():
            offset[0] += random.randint(-8, 8)
            offset[1] += random.randint(-8, 8)

        pygame.draw.rect(surface, c, pygame.Rect(self.x + offset[0], self.y + offset[1], self.width, self.height))

        if self.border:
            pygame.draw.rect(surface, (0,0,0), pygame.Rect(self.x + offset[0], self.y + offset[1], self.width, self.height), 1)

    def get_2d_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
