import unittest

from classes.guest import *
from classes.song import *
from classes.room import *

class TestRoom(unittest.TestCase):

    def setUp(self):

        self.guest_1 = Guest("Brian", "its not unusual")
        self.guest_2 = Guest("Lisa", "brass in pocket")
        self.guest_3 = Guest("Chris", "smells like teen spirit")

        self.room_1 = Room ("Pop", 5)
        self.room_2 = Room ("Rock", 3)
        self.room_3 = Room ("Jazz", 1)

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


    


    

    # 
    # def test_add_song_to_room(self):

    # def test_room_has_song(self):

    # def test_guest_has_money(self):




    


    # def test_pub_can_add_drink(self):
    #     self.pub.add_drink(self.drink_1)
    #     self.assertEqual(1, self.pub.stock_level(self.drink_1))
    #     self.assertEqual(2.00, self.pub.stock_value())

    

