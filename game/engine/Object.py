

class Object3D:
    def __init__(self, x, y, z, depth):
        self.x = x
        self.y = y
        self.z = z
        self.depth = depth

    def draw_cross_section(self, surface, offset):
        return