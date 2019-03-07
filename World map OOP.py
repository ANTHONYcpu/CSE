class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


courts = Room("NBA 2K COURTS", 'basketball_courts', 'neighborhood', "store", "clothes_store", "INSERT DESCRIPTION HERE")
basketball_courts = Room("NBA 2K 3s COURTS, NBA 2K DOTS, NBA 2K 2s COURTS")
neighborhood = Room("team practice facility","foot_locker_store","king_of_the courts","2K zone","the venue","the downtown courts")
store = Room("Doc's","Wheels","alley_oops tattoo","boost stand","foot_locker_store")
clothes_store = Room("Swag's","NBA 2K2 store")
NBA_loading_screen = Room=("play_now","black_top","my_team","freestyle")

