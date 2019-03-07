class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
class Mini(Item):
    def __init__(self):
        super(Mini, self).__init__("Mini Shield", "Small Shield Potion takes 2 seconds to consume, and upon consumption grants 25 Shield to a maximum of 50")
