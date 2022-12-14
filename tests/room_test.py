import unittest

from classes.guest import *
from classes.song import *
from classes.room import *

class TestRoom(unittest.TestCase):

    def setUp(self):

        self.guest_1 = Guest("Brian", "its not unusual", 50)
        self.guest_2 = Guest("Lisa", "brass in pocket", 100)
        self.guest_3 = Guest("Chris", "smells like teen spirit", 150)

        self.room_1 = Room ("Pop", 5, 5)
        self.room_2 = Room ("Rock", 3, 10)
        self.room_3 = Room ("Jazz", 1, 15)

        self.song_1 = Song ("Tom Jones", "Its Not Unusual")
        self.song_2 = Song ("The Pretrenders", "Brass in Pocket")
        self.song_3 = Song ("Rhianna", "Diamonds")
        self.song_4 = Song ("Nirvana", "Smells Like Teen Spirit")
        self.song_5 = Song ("Miles Davis", "Birth of the Cool")
        self.song_6 = Song ("Johnny Thunders", "Pipeline")
        self.song_7 = Song ("Scott Walker", "Jackie")

    def test_room_has_name(self):
        self.assertEqual("Pop", self.room_1.name)

    def test_room_has_a_capacity(self):
        self.assertEqual(5, self.room_1.capacity)

    def test_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        expected = 1
        actual = len(self.room_1.guests)
        self.assertEqual(actual, expected)

    def test_check_out_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_out_guest(self.guest_1)
        expected = 0
        actual = len(self.room_1.guests)
        self.assertEqual(actual, expected)

    def test_add_song_to_room(self):
        self.room_1.add_song_to_room(self.song_1)
        expected = 1
        actual = len(self.room_1.songs)
        self.assertEqual(actual, expected)

    def test_room_has_entry_fee(self):
        self.assertEqual(5, self.room_1.entry_fee)

    def test_room_till_starts_at_0(self):
        self.assertEqual(0, self.room_1.till)
    
    def test_room_charges_entry_fee(self):
        self.room_1.room_charges_entry_fee(self)
        expected = 5
        actual = self.room_1.entry_fee
        self.assertEqual(expected,actual)

    def test_remove_entry_fee_from_wallet(self):
        expected = 45
        actual = self.guest_1.remove_entry_fee_from_wallet(self.room_1.entry_fee, self.guest_1)
        self.assertEqual (expected, actual)

    # def test_max_room_capacity(self):





    

    




    

  
    # def test_room_has_song(self):

    # def test_guest_has_money(self):




    
