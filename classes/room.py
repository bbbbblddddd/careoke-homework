class Room:

    def __init__ (self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guests = []
        self.songs = []

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song_to_room(self, song):
        self.songs.append(song)
    
    
    