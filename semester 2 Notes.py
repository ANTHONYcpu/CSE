print("Hello World")

# This is a single-line commment.

cars = 5
driving = True

print("I have %d cars" % cars)
print("I have " + str(cars) + " cars")

age = input("How old are you?")
print(age + "??? You really shouldn't lie about your age.")

colors = ["blue", "orange", "yellow", "green", "cyan"]
colors.append("magenta")

print(colors)
colors.pop(0)
print(colors)

import string
print(list(string.ascii_letters))
print(string.digits)
print(string.punctuation)