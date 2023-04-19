from engine.Object import Object3D
import pygame
import random

from engine.util import glitch_color


class Cylinder(Object3D):
    def __init__(self, x, y, z, diameter, depth, color):
        self.x = x
        self.y = y
        self.z = z
        self.diameter = diameter
        self.depth = depth
        self.color = color

    def draw_cross_section(self, surface, offset):
        c = glitch_color(self.color, 0.5)
        pygame.draw.circle(surface, c, (int(self.x + self.diameter/2 + offset[0]), int(self.y + self.diameter/2 + offset[1])), int(self.diameter / 2))
        pygame.draw.circle(surface, (0,0,0), (int(self.x + self.diameter/2 + offset[0]), int(self.y + self.diameter/2 + offset[1])), int(self.diameter / 2), 1)

    def get_2d_rect(self):
        return pygame.Rect(self.x, self.y, self.diameter, self.diameter)

    def get_2d_rect_velocity(self, velocity):
        return pygame.Rect(self.x+ velocity[0], self.y+ velocity[1], self.diameter , self.diameter )
