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
    def __init__(self, pos, size, zoom_level, camera, surface):
        """.

        :param zoom_level: constant. Zoomlevel of downloaded map tile. Shouldn't be changed
        """
        self.camera = camera
        self.surface = surface
        self.zoom_level = zoom_level
        self.bbox = pos[0], pos[1], pos[0] + size, pos[1] + size

        self.last_used = None
        self.image = None
        self.rendered_image = None

    def render(self):
        if not self.image:
            self.__download_image()
        image_size = self.camera.get_screen_x_coordinate_from_GCS_coordinates(self.bbox[2]) - self.camera.get_screen_x_coordinate_from_GCS_coordinates(self.bbox[0])
        self.rendered_image = pygame.transform.scale(self.image, (image_size, image_size))
        pass



    def draw(self):
        if not self.is_visible():
            return
        self.render()
        pixel_coords = (self.camera.get_screen_coordinates_from_GCS_coordinates((self.bbox[0], self.bbox[1])))
        self.surface.blit(self.rendered_image, pixel_coords)
        pass


    def is_visible(self):
        return is_box_collision(self.bbox, self.camera.bbox)

    def clear(self):
        self.image = None

    def __download_image(self):
        print("downloading new chunk...")
        #pygame.time.wait(1000)
        map = geotiler.Map(extent=self.bbox, zoom=self.zoom_level)
        image = geotiler.render_map(map)
        image.save("map.png")
        mode = image.mode
        size = image.size
        data = image.tobytes()
        self.image = pygame.image.fromstring(data, size, mode)

        print("done!")






