class car(object):
    def __init__(self, battery, battery_left=100):
        # These are attributes that a car has.
        # These should all be relevant to our program
        self.door = True
        self.seats = 5
        self.gps = True
        self.battery = battery
        self.battery_left = battery_left

    def charge(self, time):
        self.battery_left += time
        if self.battery_left > 100:
            self.battery_left = 100

            print("You can't. The car battery is dead.")
            return
        self.battery_left -= duration * battery_loss_per_minute
        if self.battery_left < 0:
    def make_call(self, duration):
        if not self.screen:
            return
            print("You can't make a phone call.")
            print("Your screen is broken.")
        battery_loss_per_minute = 10
        if self.battery_left <= 0:
            self.battery_left = 0
            print("Your car breaks down.")
        elif self.battery_left == 0:
            print("Your car breaks down.")
        else:
            print("You successfully make the car come back on.")
            print("Your car is now at %s" % self.battery_left)

    def smash_phone(self):
        print("SMASH!!!!!!!!!!!")
        print("It broke.")
        self.screen = False

# Initialize Objects
my_car = car("bmw", 100)
your_car = car("Bell", 0)
default_car = car("bmw")

your_car.make_(10)
my_car.make_(10)
my_car.charge(50)
my_car.make_call(10)
your_car.smash_car()
your_car.make_(1)


