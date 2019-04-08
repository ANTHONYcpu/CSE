class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """This moves the player to a new room

        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room so see if a room
        exists in that direction.

        :param direction: The direction that you want to move to
        :return: The Room object if it exists, or None if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]



courts = Room("NBA 2K COURTS", 'basketball_courts', 'neighborhood', "store", "clothes_store", "INSERT DESCRIPTION HERE")
basketball_courts = Room("NBA 2K 3s COURTS, NBA 2K DOTS, NBA 2K 2s COURTS")
neighborhood = Room("team practice facility","foot_locker_store","king_of_the courts","2K zone","the venue","the downtown courts")
store = Room("Doc's","Wheels","alley_oops tattoo","boost stand","foot_locker_store")
clothes_store = Room("Swag's","NBA 2K2 store")
NBA_loading_screen = Room=("play_now","black_top","my_team","freestyle")

player = Player(R19A)

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")
