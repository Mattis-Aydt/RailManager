from model.tracks import Switch
import pygame
from view.map.map import StandardMap, Chunk
from view.map.camera import Camera

from view.config import RESOLUTION, PRELOAD_FACTOR


win = pygame.display.set_mode(RESOLUTION)
switch = Switch((100, 100))

map = StandardMap(win)
cam = Camera(None, None, RESOLUTION)
cam.bbox = 8.360948, 48.992639, 8.360948 + 0.4, 48.992639 + 0.4
chunk1 = Chunk((8.360948, 48.992639), 0.3, 12, cam, win)
chunk2 = Chunk((8.360948 + 0.3, 48.992639), 0.3, 12, cam, win)
chunk3 = Chunk((8.360948 + 0.7, 48.992639), 0.3, 12, cam, win)
chunk4 = Chunk((8.360948 + 1, 48.992639), 0.3, 12, cam, win)







run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255, 255, 255))
    chunk1.draw()
    chunk2.draw()
    chunk3.draw()
    chunk4.draw()



    """
    for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL:
            map.zoom(event.y*map.get_image_zoom()*.2)
            
         """
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        cam.move_up(0.01)
    if keys[pygame.K_a]:
        cam.move_left(0.01)
    if keys[pygame.K_s]:
        cam.move_down(0.01)
    if keys[pygame.K_d]:
        cam.move_right(0.01)


    pygame.display.update()
    pygame.time.wait(10)
