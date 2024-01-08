import unittest
from src.model.tracks import Track, Incomplete_track, Piece

class Test_Incomplete_tracks(unittest.TestCase):

    def test_add_remove_piece(self):
        track = Incomplete_track(None, None)
        piece = Piece(123.123, 456.678)
        track.add_piece(piece)
        self.assertEqual(len(track.pieces), 1)
        track.add_piece(piece)
        self.assertEqual(len(track.pieces), 2)
        self.assertEqual(type(track.pieces[0]), Piece)
        track.remove_piece()
        self.assertEqual(len(track.pieces), 1)





