from model.tracks import Switch
import pygame
from view.map.map import StandardMap
from view.config import RESOLUTION, PRELOAD_FACTOR

print("Hello World!")
win = pygame.display.set_mode(RESOLUTION)
switch = Switch((100, 100))

map = StandardMap(win, render_size=(int(RESOLUTION[0]*PRELOAD_FACTOR), int(RESOLUTION[1]*PRELOAD_FACTOR)))
map.set_dimensions((1, 1), (0, 0))
flip_flop = True

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255, 255, 255))
    map.draw()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL:
            map.zoom(event.y*map.get_image_zoom()*.2)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        map.change_offset(0, 10)
    if keys[pygame.K_a]:
        map.change_offset(10, 0)
    if keys[pygame.K_s]:
        map.change_offset(0, -10)
    if keys[pygame.K_d]:
        map.change_offset(-10, 0)


    pygame.display.update()
    pygame.time.wait(10)