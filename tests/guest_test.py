import unittest

from classes.guest import *

class TestGuest(unittest.TestCase):
    def setUp (self):
        self.guest_1 = Guest("Brian", "its not unusual", 50)

    def test_guest_has_a_name(self):
        self.assertEqual("Brian", self.guest_1.name)

    def test_guest_has_a_favourite_song(self):
        self.assertEqual("its not unusual", self.guest_1.favourite_song)

    def test_guest_has_money(self):
        self.assertEqual(50, self.guest_1.wallet)
    
    