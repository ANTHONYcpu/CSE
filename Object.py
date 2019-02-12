class Phone(object):
    def __init__(self, carrier, charge_left):
        # These are attributes that a phone has.
        # These should all be relevant to our program
        self.screen = True
        self.camera = 2
        self.microphone = True
        self.carrier = carrier
        self.battery_left = charge_left

        def charge(self, time):
            self.battery_left +=