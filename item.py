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
        super(Mini, self).__init__("Mini Shield", "Small Shield Potion takes 2 seconds to consume, and upon consumption grants 25 Shield to a maximum of 50")


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
        super(HeavyAssaultRifle, self).__init__("HeavyAssaultRifle", "The weapon should be tap-fired for maximum accuracy and damage. It uses Medium Bullets", 48)

class PumpShotgun(Weapon):
    def __init__(self, name,description, quantity=1):
        super(PumpShotgun, self).__init__("PumpShotgun", "The it uses Shells 'n' Slugs.", 110 )