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
    def __init__(self, name, description, quantity=1):
        super(PumpShotgun, self).__init__("PumpShotgun", "The PumpShotgun it uses Shells 'n' Slugs.", 110 )

class DualPistol(Weapon):
    def __init__(self, name, description, quantity=1):
        super(DualPistol, self).__init__("Dual_Pistol", "Both pistols fire with one pull of the trigger. They use Medium Bullets", 43)

class SubmachineGun(Weapon):
    def __init__(self, name, description, quantity=1):
        super(SubmachineGun, self).__init__("SubmachineGun", "It is available in Common, Uncommon, and Rare variants", 19)

class RocketLauncher(Weapon):
    def __init__(self, name, description, quantity=1):
        super(RocketLauncher, self).__init__("RocketLauncher", "It does not consume ammo but instead rapidly consumes its durability", 121)

class HuntingRifle(Weapon):
    def __init__(self, name, description, quantity=1):
        super(HuntingRifle, self).__init__("HuntingRifle", "Hunting Rifle is a Sniper Rifle in Battle Royale. It is available in Uncommon and Rare variants. It uses Heavy Bullets", 90)

class HandCannon(Weapon):
    def __init__(self, name, description, quantity=1):
        super(HandCannon, self).__init__("HandCannon", "It uses Heavy Bullets", 78)

class HeavySniper(Weapon):
    def __init__(self, name, description, quantity=1):
        super(HeavySniper, self).__init__("HeavySniper", "It delivers devastating damage at the cost of having a long reload time", 157)