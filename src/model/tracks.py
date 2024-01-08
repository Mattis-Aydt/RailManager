import pygame
from view_mode import View_mode

class Track:
    def __init__(self, pieces):
        self.pieces = pieces


class Switch:

    def __init__(self, position):
        self.pos = position


    def draw(self, surface, view_mode):
        pass


class Incomplete_track:
    def __init__(self, start_switch, end_switch):
        self.pieces = []
        self.start_switch = start_switch
        self.end_switch = end_switch

    def add_piece(self, piece):
        self.pieces.append(piece)

    def remove_piece(self):
        self.pieces.pop()

    def get_complete_track(self):
        if len(self.pieces) == 0:
            raise Exception("Track can't be completed, because it has no pieces")
        if self.start_switch.position != self.pieces[0].point1:
            raise Exception("Track can't be completed, first piece doesnt start at starting_switch")
        if self.end_switch.position != self.pieces[-1].point2:
            raise Exception("Track can't be completed, last piece doesnt end at end_switch")


class Piece:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.maxSpeed = 0
