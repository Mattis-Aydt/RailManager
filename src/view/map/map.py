import geotiler
import pygame





class StandardMap:
    def __init__(self, surface, render_size=(1920, 1080), zoom=6, center=(10.0, 51.0)):
        self.__surface = surface
        self.__render_size = render_size
        self.__zoom = zoom
        self.__center = center
        self.__base_map = None
        self.__base_map_image = None
        self.__base_map_pygame_image = None
        self.__base_map_pygame_image_zoomed = None
        self.__update_base_map()






    def draw(self, scale, offset):
        self.__surface.blit(self.__base_map_pygame_image_zoomed, (0, 0))
        pass

    def update(self):
        pass

    def zoom(self, amount):
        previous_zoom = self.__zoom
        self.__zoom += amount
        if int(previous_zoom) != int(self.__zoom):
            self.__update_base_map()



        self.set_pygame_image_zoomed()





    def __update_base_map(self):
        print("downloading new map...")
        #pygame.time.wait(1000)
        self.__base_map = geotiler.Map(center=self.__center, zoom=int(self.__zoom), size=self.__render_size)
        self.__base_map_image = geotiler.render_map(self.__base_map)
        self.set_pygame_image()
        self.set_pygame_image_zoomed()
        print("done!")




    def set_pygame_image(self):
        mode = self.__base_map_image.mode
        size = self.__base_map_image.size
        data = self.__base_map_image.tobytes()
        self.__base_map_pygame_image = pygame.image.fromstring(data, size, mode)

    def set_pygame_image_zoomed(self):
        map_zoom = int(self.__zoom)
        image_zoom = 1 + (self.__zoom - map_zoom)
        print(image_zoom)
        self.__base_map_pygame_image_zoomed = pygame.transform.scale_by(self.__base_map_pygame_image, (image_zoom, image_zoom))
