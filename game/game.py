import pygame
pygame.init()

import sys

from engine.Cuboid import Cuboid
from engine.Cylinder import Cylinder
from engine.renderer import *
map = [
    "                         ",
    "                         ",
    "                         ",
    "                         ",
    "                    #    ",
    "                    # ## ",
    "#                   #    ",
    "#                   #    ",
    "#    ####  ####     #    ",
    "#                   #    ",
    "#########################"

]

TILE_SIZE = 32
screen_size = (TILE_SIZE*(len(map[0])), TILE_SIZE*(len(map)))
screen = pygame.display.set_mode(screen_size)

assert isinstance(screen, object)
render = PerspectiveRender(screen)

objects = []

player = {
        "object": Cylinder(0, 0, 16, TILE_SIZE, 24, (250, 100, 0)),

    "velocity": [0,0],
    "onground": False
}

frameclock = pygame.time.Clock()

keys = pygame.key.get_pressed()
last_keys = pygame.key.get_pressed()


def load_map(map):
    y = 0
    for line in map:
        x = 0
        for tile in line:
            if tile == "#":
                objects.append(Cuboid(TILE_SIZE * x, TILE_SIZE * y, 0, TILE_SIZE, TILE_SIZE, TILE_SIZE*2, (64, 100, 64)))
            x += 1
        y += 1

load_map(map)
def update():
    global keys, last_keys, render

    max_value = 1

    mouse = pygame.mouse.get_pos()
    p = [
        ( screen_size[0] / 2 - pygame.mouse.get_pos()[0] ) / screen_size[0] * max_value,
        (screen_size[1] / 2 - pygame.mouse.get_pos()[1]) / screen_size[1] * max_value
    ]
    render.set_perspective(p[0], p[1])

    if keys[pygame.K_d]:
        player["velocity"][0] = +4
    elif keys[pygame.K_a]:
        player["velocity"][0] = -4
    else:
        player["velocity"][0] = 0

    if keys[pygame.K_w] and player["onground"]:
        player["velocity"][1] = -24

    if not player["onground"]:
        player["velocity"][1] += 4


    collide_y = False
    recty = player["object"].get_2d_rect_velocity([0, player["velocity"][1]])
    for ob in objects:
        if ob.get_2d_rect().colliderect(recty):
            collide_y = True

    if not collide_y:
        player["object"].y += player["velocity"][1]
        player["onground"] = False
    else:
        player["velocity"][1] = 0
        player["onground"] = True


    collide_x = False
    rectx = player["object"].get_2d_rect_velocity([player["velocity"][0], 0])
    for ob in objects:
        if ob.get_2d_rect().colliderect(rectx):
            collide_x = True

    if not collide_x:
        player["object"].x += player["velocity"][0]
    else:
        player["velocity"][0] = 0


def draw():
    global screen, render
    screen.fill((100, 100, 255))
    render.add_objects(objects)
    render.add_object(player["object"])

    render.render()


while True:
    last_keys = keys
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    update()
    draw()

    pygame.display.flip()
    frameclock.tick(30)
