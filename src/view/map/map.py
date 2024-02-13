import threading

import geotiler
import pygame
from geotiler import render_map_async

from src.math.collisions import is_box_collision
from src.view.config import RESOLUTION, PRELOAD_FACTOR
from src.view.map.camera import Camera
from src.view.colors import *
import asyncio






class StandardMap:
    def __init__(self, surface, chunk_size=0.3):
        self.__surface = surface
        self.cam = Camera(RESOLUTION, (8.560948, 49.192639))
        self.chunk_size = chunk_size
        self.max_chunks = 1000
        self.__chunks = []
        self.chunks_to_download = []
        self.base_color = WHITE

        self.__restart_chunk_download_ticks = 200

    def generate_chunks(self):
        zoom_level = int(self.cam.zoom - 0.5)
        chunk_size = self.chunk_size * 100 * 1/pow(2, zoom_level-4)
        chunks_per_row = int(self.cam.get_bbox_width() / chunk_size) + 2
        chunk_start_x = self.cam.bbox[0] - (self.cam.bbox[0] % chunk_size)
        chunk_start_y = self.cam.bbox[1] - (self.cam.bbox[1] % chunk_size)
        for i in range(chunks_per_row):
            for j in range(chunks_per_row):
                possible_chunk_p1 = (chunk_start_x + i*chunk_size, chunk_start_y + j*chunk_size)
                chunk_exists = False
                for existing_chunk in self.__chunks:
                    if not existing_chunk.zoom_level == zoom_level:
                        continue
                    if (existing_chunk.bbox[0], existing_chunk.bbox[1]) == possible_chunk_p1:
                        chunk_exists = True
                        break

                if not chunk_exists:
                    chunk = Chunk(possible_chunk_p1, chunk_size, zoom_level, self.cam, self.__surface)
                    self.__chunks.append(chunk)
                    self.chunks_to_download.append(chunk)
        self.cleanup_chunks()

    def cleanup_chunks(self):
        while len(self.__chunks) > self.max_chunks:
            chunk = self.__chunks.pop(0)
            chunk.clear()

    def draw(self):
        self.generate_chunks()
        self.__surface.fill(self.base_color)
        for chunk in self.__chunks:
            if chunk.zoom_level == int(self.cam.zoom-0.5):
                chunk.draw()

    def update(self):
        for chunk in self.chunks_to_download:
            task = asyncio.create_task(chunk.download_chunk_async())
            self.chunks_to_download.remove(chunk)

        self.check_downloads()

    def check_downloads(self):
        for chunk in self.__chunks:
            if chunk.ticks_scince_downloading > self.__restart_chunk_download_ticks:
                chunk.ticks_scince_downloading = 0
                task = asyncio.create_task(chunk.download_chunk_async())
                print("redownloading chunk...")




class Chunk:
    def __init__(self, pos, size, zoom_level, camera, surface):
        """.

        :param zoom_level: constant. Zoomlevel of downloaded map tile. Shouldn't be changed
        """
        self.camera = camera
        self.surface = surface
        self.window_size = self.camera.screen_size
        self.zoom_level = zoom_level
        self.bbox = pos[0], pos[1], pos[0] + size, pos[1] + size

        self.last_used = None
        self.image = None
        self.rendered_image = None
        self.is_downloading = False
        self.ticks_scince_downloading = 0

    def render(self):
        if not self.image:
            self.ticks_scince_downloading += 1
            return
        image_size = self.camera.get_screen_x_coordinate_from_GCS_coordinate(self.bbox[2]) - self.camera.get_screen_x_coordinate_from_GCS_coordinate(self.bbox[0])
        self.rendered_image = pygame.transform.scale(self.image, (image_size, image_size))
        pass


    def draw(self):
        if not self.is_visible():
            return
        self.render()
        if not self.rendered_image:
            return

        pixel_coords = (self.camera.get_screen_coordinates_from_GCS_coordinates((self.bbox[0], self.bbox[1])))
        pixel_coords_y_reversed = pixel_coords[0], self.window_size[1] - pixel_coords[1] - self.rendered_image.get_height()


        self.surface.blit(self.rendered_image, pixel_coords_y_reversed)
        pass

    def is_visible(self):
        return is_box_collision(self.bbox, self.camera.bbox)

    def clear(self):
        self.image = None

    async def download_chunk_async(self):
        # pygame.time.wait(1000)
        map = geotiler.Map(extent=self.bbox, zoom=self.zoom_level)
        image = await geotiler.render_map_async(map)
        mode = image.mode
        size = image.size
        data = image.tobytes()
        self.image = pygame.image.fromstring(data, size, mode)







