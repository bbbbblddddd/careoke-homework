class Room:

    def __init__ (self, name, capacity, entry_fee):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.till = 0
        self.guests = []
        self.songs = []

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song_to_room(self, song):
        self.songs.append(song)
    
    def remove_entry_fee_from_wallet(self, guest, entry_fee):
        self.guest.wallet -= entry_fee






    






   

    

    