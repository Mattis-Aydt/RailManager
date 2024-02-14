import time

from model.tracks import Switch
import pygame
import geotiler
from view.map.map import StandardMap, Chunk
from view.map.camera import Camera


from view.config import RESOLUTION, PRELOAD_FACTOR
import asyncio


async def main_loop(map):
    time_delta = 0
    run = True
    while run:
        time_before_tick = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        map.draw()
        map.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            map.cam.move_up(1*time_delta)
        if keys[pygame.K_a]:
            map.cam.move_left(1*time_delta)
        if keys[pygame.K_s]:
            map.cam.move_down(1*time_delta)
        if keys[pygame.K_d]:
            map.cam.move_right(1*time_delta)

        if keys[pygame.K_SPACE]:
            map.cam.zoom_by(-2.5*time_delta)
        if keys[pygame.K_LSHIFT]:
            map.cam.zoom_by(2.5*time_delta)

        await asyncio.sleep(.005)
        pygame.display.update()
        time_after_tick = time.time()
        time_delta = time_after_tick - time_before_tick
        print(1/time_delta)



win = pygame.display.set_mode(RESOLUTION)
map = StandardMap(win)
asyncio.run(main_loop(map))















