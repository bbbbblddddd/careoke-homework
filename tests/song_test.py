import unittest

from classes.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Tom Jones", "Its Not Unusual")

    def test_song_has_a_title(self):
        self.assertEqual("Its Not Unusual", self.song_1.title)

    def test_song_has_artist(self):
        self.assertEqual("Tom Jones", self.song_1.artist)

    