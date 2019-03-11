class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Consumable(Item):
    def __init__(self,name, description, quantity=1):
        super(Consumable, self).__init__(name)
        self.description = description
        self.quantity = quantity
        
class Mini(Consumable):
    def __init__(self):
        super(Mini, self).__init__("Mini Shield", "Small Shield Potion takes 2 seconds to consume, and upon consumption grants 25 Shield to a maximum of 50")
        super =("Mini 25 shield")
        def __init__(description):
            super(Mini, description) ("if you drink 1 Mini you would go up 25 shield, if you drink 2 Mini you would go up 50 shield")
