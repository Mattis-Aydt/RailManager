import unittest
from src.model.tracks import Incomplete_track, Straight_piece, Curved_piece

class Test_Incomplete_tracks(unittest.TestCase):

    def test_add_remove_piece(self):
        track = Incomplete_track()
        piece = Straight_piece(123.123, 456.678)
        track.add_piece(piece)
        self.assertEquals(len(track.pieces), 1)
        track.add_piece(piece)
        self.assertEquals(len(track.pieces), 2)
        track.remove_piece()
        self.assertEquals(len(track.pieces), 1)


    def test_check_tracks(self):
        track = Incomplete_track()

        # Empty track should return True
        self.assertTrue(track.check_track())

        # Should return true if first piece is Straight
        track = Incomplete_track()
        piece = Straight_piece(123123.123, 122331.123)
        track.add_piece(piece)
        self.assertTrue(track.check_track())

        # Should return false if first piece is Curved
        track = Incomplete_track()
        piece = Curved_piece(123123.123, 122331.123)
        track.add_piece(piece)
        self.assertFalse(track.check_track())

        # Should return True if starting with straight piece and switching back and forth
        track = Incomplete_track()
        for i in range(21):
            piece = Straight_piece(123123.123, 122331.123)
            track.add_piece(piece)
            piece = Curved_piece(123123.123, 122331.123)
            track.add_piece(piece)
        self.assertTrue(track.check_track())

        # Should return False if random piece is not Switching back and forth
        track = Incomplete_track()
        for i in range(5):
            piece = Straight_piece(123123.123, 122331.123)
            track.add_piece(piece)
            piece = Curved_piece(123123.123, 122331.123)
            track.add_piece(piece)
        wrong_piece = Curved_piece(123123.1231, 123123.123)

        track.add_piece(wrong_piece)

        for i in range(5):
            piece = Straight_piece(123123.123, 122331.123)
            track.add_piece(piece)
            piece = Curved_piece(123123.123, 122331.123)
            track.add_piece(piece)

        self.assertFalse(track.check_track())


