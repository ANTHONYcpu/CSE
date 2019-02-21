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
neighborhoods = Room("team practice facility","foot locker store","king of the courts","2K zone","the venue","the downtown courts")
store = Room("shose","gear","hoildayclothes","headbands","wristbands")
clothes_store = Room("shirts","pants","shorts","hats","jackets")