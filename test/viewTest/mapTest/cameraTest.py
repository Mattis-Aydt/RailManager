import unittest
from src.view.map.camera import Camera

class Test_Camera(unittest.TestCase):

    def test_basic_get_screen_coordinates_from_GCS_coordinates(self):
        c = Camera(None, None, (100, 100))
        c.bbox = (0, 0, 10, 10)
        self.assertEqual((50, 50), c.get_screen_coordinates_from_GCS_coordinates((5, 5)))

    def test_advanced_get_screen_coordinates_from_GCS_coordinates(self):
        c = Camera(None, None, (800, 600))
        c.bbox = (10, 10, 30, 30)
        self.assertEqual((400, 300), c.get_screen_coordinates_from_GCS_coordinates((20, 20)))





