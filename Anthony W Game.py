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


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Consumable(Item):
    def __init__(self, name, description, quantity=1):
        super(Consumable, self).__init__(name, description)
        self.quantity = quantity


class Mini(Consumable):
    def __init__(self):
        super(Mini, self).__init__("Mini Shield",
                                   "Small Shield Potion takes 2 seconds to consume, and upon consumption grants 25 Shield to a maximum of 50")


class SlurpJuice(Consumable):
    def __init__(self):
        super(SlurpJuice, self).__init__("SlurpJuice",
                                         "Slurp Juice grants one health every 0.5 seconds, up to a total of 75")


class MedKit(Consumable):
    def __init__(self):
        super(MedKit, self).__init__("MedKit, MedKit drop in stacks of 1 with a maximum stack size of 3")


class Weapon(Item):
    def __init__(self, name, description, damage):
        super(Weapon, self).__init__(name, description)
        self.damage = damage


class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class Character(object):
    def __init(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor


class Mini_gun(Weapon):
    def __init__(self, name, description, quantity=1):
        super(Mini_gun, self).__init__("Mini_gun", "It uses Light Bullets. Upon firing the Minigun, there is a "
                                                   "short delay before it begins to shoot bullets.", 18)


class HeavyAssaultRifle(Weapon):
    def __init__(self, name, description, quantity=1):
        super(HeavyAssaultRifle, self).__init__("HeavyAssaultRifle",
                                                "The weapon should be tap-fired for maximum accuracy and damage. It uses Medium Bullets",
                                                48)


class PumpShotgun(Weapon):
    def __init__(self, name, description, quantity=1):
        super(PumpShotgun, self).__init__("PumpShotgun", "The PumpShotgun it uses Shells 'n' Slugs.", 110)


class DualPistol(Weapon):
    def __init__(self, name, description, quantity=1):
        super(DualPistol, self).__init__("Dual_Pistol",
                                         "Both pistols fire with one pull of the trigger. They use Medium Bullets", 43)


class SubmachineGun(Weapon):
    def __init__(self, name, description, quantity=1):
        super(SubmachineGun, self).__init__("SubmachineGun", "It is available in Common, Uncommon, and Rare variants",
                                            19)


class RocketLauncher(Weapon):
    def __init__(self, name, description, quantity=1):
        super(RocketLauncher, self).__init__("RocketLauncher",
                                             "It does not consume ammo but instead rapidly consumes its durability",
                                             121)


class HuntingRifle(Weapon):
    def __init__(self, name, description, quantity=1):
        super(HuntingRifle, self).__init__("HuntingRifle",
                                           "Hunting Rifle is a Sniper Rifle in Battle Royale. It is available in Uncommon and Rare variants. It uses Heavy Bullets",
                                           90)


class HandCannon(Weapon):
    def __init__(self, name, description, quantity=1):
        super(HandCannon, self).__init__("HandCannon", "It uses Heavy Bullets", 78)


class HeavySniper(Weapon):
    def __init__(self, name, description, quantity=1):
        super(HeavySniper, self).__init__("HeavySniper",
                                          "It delivers devastating damage at the cost of having a long reload time",
                                          157)


class GrenadeLauncher(Weapon):
    def __init__(self, name, description, quantity=1):
        super(GrenadeLauncher, self).__init__("GrenadeLauncher",
                                              "It does not consume ammo but instead rapidly consumes its durability",
                                              110)


class TacticalShotGun(Weapon):
    def __init__(self, name, description, quantity=1):
        super(TacticalShotGun, self).__init__("TacticalShotGun", "It uses Shells 'n' Slugs", 74)


courts = Room("NBA 2K COURTS", 'basketball_courts', 'neighborhood', "store", "clothes_store", "INSERT DESCRIPTION HERE")
basketball_courts = Room("NBA 2K 3s COURTS, NBA 2K DOTS, NBA 2K 2s COURTS")
neighborhood = Room("team practice facility","foot_locker_store","king_of_the courts","2K zone","the venue","the downtown courts")
store = Room("Doc's","Wheels","alley_oops tattoo","boost stand","foot_locker_store")
clothes_store = Room("Swag's","NBA 2K2 store")
NBA_loading_screen = Room=("play_now","black_top","my_team","freestyle")

player = Player(courts)

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
