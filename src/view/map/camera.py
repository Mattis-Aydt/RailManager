class Camera:
    def __init__(self, pos, zoom, screen_size):
        self.pos = pos
        self.zoom = zoom
        self.screen_size = screen_size
        self.bbox = None

    def get_screen_coordinates_from_GCS_coordinates(self, point):
        x = point[0]
        y = point[1]
        return self.get_screen_x_coordinate_from_GCS_coordinates(x), self.get_screen_y_coordinate_from_GCS_coordinates(y)

    def get_screen_x_coordinate_from_GCS_coordinates(self, x):
        return ((x - self.bbox[0]) / (self.bbox[2] - self.bbox[0])) * self.screen_size[0]
    def get_screen_y_coordinate_from_GCS_coordinates(self, y):
        return -((y - self.bbox[1]) / (self.bbox[3] - self.bbox[1])) * self.screen_size[1]

    def move_right(self, amount):
        self.bbox = (self.bbox[0] + amount, self.bbox[1], self.bbox[2] + amount, self.bbox[3])

    def move_left(self, amount):
        self.bbox = (self.bbox[0] - amount, self.bbox[1], self.bbox[2] - amount, self.bbox[3])

    def move_up(self, amount):
        self.bbox = (self.bbox[0], self.bbox[1] + amount, self.bbox[2], self.bbox[3] + amount)

    def move_down(self, amount):
        self.bbox = (self.bbox[0], self.bbox[1] - amount, self.bbox[2], self.bbox[3] - amount)

