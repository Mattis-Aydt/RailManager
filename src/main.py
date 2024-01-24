from model.tracks import Switch
import pygame
from view.map.map import StandardMap

print("Hello World!")
win = pygame.display.set_mode((800, 800))
switch = Switch((100, 100))

map = StandardMap(win, render_size=(800, 800))
flip_flop = True

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255, 255, 255))
    map.draw((0, 0), (1, 1))
    map.zoom(0.01)



    pygame.display.update()
    pygame.time.wait(10)