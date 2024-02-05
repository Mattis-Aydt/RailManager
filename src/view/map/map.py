import geotiler
import pygame
from src.math.collisions import is_box_collision
from src.view.config import RESOLUTION, PRELOAD_FACTOR
import threading





class StandardMap:
    def __init__(self, surface):
        self.__surface = surface
        self.__scale = (1, 1)
        self.offset = (0, 0)
        self.__render_quality_chunk = ()

        self.__chunks = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] #16-zoom levels
        self.__current_chunks_scaled = []
        self.__zoom = 6


    def set_scale(self, x, y):
        self.__scale = (x, y)
        #update function smth

    def zoom(self, factor):
        pass


    def __update_chunks(self):
        pass


    def __set_pygame_image(self, geotiler_image):
        mode = geotiler_image.mode
        size = geotiler_image.size
        data = geotiler_image.tobytes()
        return pygame.image.fromstring(data, size, mode)


class Chunk:
    def __init__(self, bbox, zoom_level, camera, surface):
        """.

        :param zoom_level: constant. Zoomlevel of downloaded map tile. Shouldn't be changed
        """
        self.camera = camera
        self.surface = surface
        self.zoom_level = zoom_level
        self.bbox = bbox

        self.last_used = None
        self.rendered_image = None

    def render(self):
        if not self.rendered_image:
            self.__download_image()



    def draw(self, map_size):
        if not self.is_visible(map_size):
            return
        if not self.rendered_image:
            self.render()
    def is_visible(self, map_size):
        return is_box_collision(self.bbox, self.camera.bbox)

    def clear(self):
        self.rendered_image = None

    def __download_image(self):
        print("downloading new chunk...")
        #pygame.time.wait(1000)
        self.__base_map = geotiler.Map(extent=self.bbox, zoom=self.zoom_level)
        self.__base_map_image = geotiler.render_map(self.__base_map)
        print("done!")

class Camera:
    def __init__(self, pos, zoom):
        self.pos = pos
        self.zoom = zoom
        self.bbox = None

