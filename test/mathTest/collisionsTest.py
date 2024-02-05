import unittest
from src.math.collisions import is_line_collision, is_box_collision

class Test_Line_Collision(unittest.TestCase):

    def test_line_collision_a_left(self):
        self.assertTrue(is_line_collision((1, 3), (2, 4)))
        self.assertFalse(is_line_collision((1, 2), (3, 4)))

    def test_line_collision_a_right(self):
        self.assertTrue(is_line_collision((2, 4), (1, 3)))
        self.assertFalse(is_line_collision((3, 4), (1, 2)))

    def test_line_collision_a_inside_b(self):
        self.assertTrue(is_line_collision((2, 3), (1, 4)))

    def test_line_collision_b_inside_a(self):
        self.assertTrue(is_line_collision((1, 4), (2, 3)))

class Test_Box_Collision(unittest.TestCase):

    def test_a_left(self):
        self.assertTrue(is_box_collision((1, 0, 3, 10), (2, 0, 4, 10)))
        self.assertFalse(is_box_collision((1, 0, 2, 10), (3, 4, 4, 12)))
        self.assertFalse(is_box_collision((1, 0, 3, 2), (2, 4, 4, 12)))

    def test_a_right(self):
        self.assertTrue(is_box_collision((2, 0, 4, 10), (1, 0, 3, 10)))
        self.assertFalse(is_box_collision((3, 0, 4, 10), (1, 2, 2, 12)))
        self.assertFalse(is_box_collision((2, -10, 4, -2), (1, 4, 3, 12)))

    def test_a_inside_b(self):
        self.assertTrue(is_box_collision((1, 0, 2, 1), (0, -1, 3, 2)))

    def test_b_inside_a(self):
        self.assertTrue(is_box_collision((0, -1, 3, 2), (1, 0, 2, 1)))
