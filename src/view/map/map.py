import geotiler
import pygame
from src.math.collisions import is_box_collision
from src.view.config import RESOLUTION, PRELOAD_FACTOR
from src.view.map.camera import Camera
import threading





class StandardMap:
    def __init__(self, surface):
        self.__surface = surface
        self.__cam = Camera(RESOLUTION)

        self.__chunks = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        self.__current_chunks_scaled = []


    def zoom(self, amount):
        self.__cam.zoom(amount)


    def __update_chunks(self):
        pass


    def __set_pygame_image(self, geotiler_image):
        mode = geotiler_image.mode
        size = geotiler_image.size
        data = geotiler_image.tobytes()
        return pygame.image.fromstring(data, size, mode)


class Chunk:
    def __init__(self, pos, size, zoom_level, camera, surface, window_size):
        """.

        :param zoom_level: constant. Zoomlevel of downloaded map tile. Shouldn't be changed
        """
        self.camera = camera
        self.surface = surface
        self.window_size = window_size
        self.zoom_level = zoom_level
        self.bbox = pos[0], pos[1], pos[0] + size, pos[1] + size

        self.last_used = None
        self.image = None
        self.rendered_image = None

    def render(self):
        if not self.image:
            self.__download_image()
        image_size = self.camera.get_screen_x_coordinate_from_GCS_coordinate(self.bbox[2]) - self.camera.get_screen_x_coordinate_from_GCS_coordinate(self.bbox[0])
        self.rendered_image = pygame.transform.scale(self.image, (image_size, image_size))
        pass



    def draw(self):
        if not self.is_visible():
            return
        self.render()
        pixel_coords = (self.camera.get_screen_coordinates_from_GCS_coordinates((self.bbox[0], self.bbox[1])))
        pixel_coords_y_reversed = pixel_coords[0], self.window_size[1] - pixel_coords[1] - self.rendered_image.get_height()
        self.surface.blit(self.rendered_image, pixel_coords_y_reversed)
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






