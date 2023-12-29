import pygame

class Track:
    def __init__(self, pieces):
        self.pieces = pieces



class Incomplete_track:
    def __init__(self, start_switch, end_switch):
        self.pieces = []
        self.start_switch = start_switch
        self.end_switch = end_switch

    def check_track(self):
        is_straight = False
        for piece in self.pieces:
            if is_straight and type(piece) is Straight_piece:
                return False
            if not is_straight and type(piece) is Curved_piece:
                return False
            is_straight = not is_straight
        return True

    def add_piece(self, piece):
        self.pieces.append(piece)

    def remove_piece(self):
        self.pieces.pop()

    def get_complete_track(self):
        if len(self.pieces) == 0:
            raise Exception("Track can't be completed, because it has no pieces")
        if not self.check_track():
            raise Exception("Track can't be completed, because self.check_track doesnt return True")
        if self.start_switch.position != self.pieces[0].point1:
            raise Exception("Track can't be completed, first piece doesnt start at starting_switch")
        if self.end_switch.position != self.pieces[-1].point2:
            raise Exception("Track can't be completed, last piece doesnt end at end_switch")



class Straight_piece:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.max_speed = float("inf")


class Curved_piece:
    def __init__(self, point1, point2, curve_point):
        self.point1 = point1
        self.point2 = point2
        self.curve_point = curve_point
        self.max_speed = self.__get_max_speed()

    def __get_max_speed(self):
        # TODO
        return .0
