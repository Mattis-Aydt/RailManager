from model.tracks import Switch
import pygame
import geotiler
from view.map.map import StandardMap, Chunk
from view.map.camera import Camera

from view.config import RESOLUTION, PRELOAD_FACTOR
import asyncio

async def main_loop(map):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        map.draw()
        map.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            map.cam.move_up(0.04)
        if keys[pygame.K_a]:
            map.cam.move_left(0.04)
        if keys[pygame.K_s]:
            map.cam.move_down(0.04)
        if keys[pygame.K_d]:
            map.cam.move_right(0.04)

        if keys[pygame.K_SPACE]:
            map.cam.zoom_by(-0.1)
        if keys[pygame.K_LSHIFT]:
            map.cam.zoom_by(0.1)

        await asyncio.sleep(.001)
        pygame.display.update()



win = pygame.display.set_mode(RESOLUTION)
map = StandardMap(win)
asyncio.run(main_loop(map))















