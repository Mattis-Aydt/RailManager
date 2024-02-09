class Camera:
    def __init__(self, screen_size, pos=(8.560948, 49.192639), zoom=12):
        self.pos = pos
        self.zoom = zoom
        self.screen_size = screen_size
        self.bbox = None
        self.set_bbox()

    def get_screen_coordinates_from_GCS_coordinates(self, point):
        x = point[0]
        y = point[1]
        return self.get_screen_x_coordinate_from_GCS_coordinate(x), self.get_screen_y_coordinate_from_GCS_coordinate(y)

    def get_screen_x_coordinate_from_GCS_coordinate(self, x):
        return ((x - self.bbox[0]) / (self.bbox[2] - self.bbox[0])) * self.screen_size[0]
    def get_screen_y_coordinate_from_GCS_coordinate(self, y):
        return ((y - self.bbox[1]) / (self.bbox[3] - self.bbox[1])) * self.screen_size[1]

    def get_GCS_coordinates_from_screen_coordinates(self, point):
        pass
        #TODO

    def get_GCS_x_coordinate_from_screen_coordinate(self, x):
        pass
        #TODO

    def get_GCS_y_coordinate_from_screen_coordinate(self, y):
        pass
        #TODO



    def move_right(self, amount):
        self.pos = self.pos[0] + (amount * 100 * 1/pow(2, self.zoom-4)), self.pos[1]
        self.set_bbox()

    def move_left(self, amount):
        self.pos = self.pos[0] - (amount * 100 * 1/pow(2, self.zoom-4)), self.pos[1]
        self.set_bbox()

    def move_up(self, amount):
        self.pos = self.pos[0], self.pos[1] + (amount * 100 * 1/pow(2, self.zoom-4))
        self.set_bbox()

    def move_down(self, amount):
        self.pos = self.pos[0], self.pos[1] - (amount * 100 * 1/pow(2, self.zoom-4))
        self.set_bbox()

    def zoom_by(self, amount):
        self.zoom += amount
        self.set_bbox()

    def set_bbox(self):
        size = 100 * 1/pow(2, self.zoom-4)
        self.bbox = self.pos[0] - size/2, self.pos[1] - size/2, self.pos[0] + size/2, self.pos[1] + size/2


