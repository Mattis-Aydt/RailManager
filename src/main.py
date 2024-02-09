from model.tracks import Switch
import pygame
from view.map.map import StandardMap, Chunk
from view.map.camera import Camera

from view.config import RESOLUTION, PRELOAD_FACTOR


win = pygame.display.set_mode(RESOLUTION)
switch = Switch((100, 100))

map = StandardMap(win)
cam = Camera(RESOLUTION)

chunks = []
for i in range(30):
    for j in range(30):
        chunks.append(Chunk((8.360948 + 0.099*(i-5), 48.992639 + 0.099*(j-5)), 0.1, 12, cam, win, RESOLUTION))







run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255, 255, 255))
    for chunk in chunks:
        chunk.draw()




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

    if keys[pygame.K_SPACE]:
        cam.zoom_by(-0.1)
    if keys[pygame.K_LSHIFT]:
        cam.zoom_by(0.1)


    pygame.display.update()

