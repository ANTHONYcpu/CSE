import random

print("Lucky 7s!")
print("Round: 1")

playing = True
round = 1
money = 15
while money > 0:
    Dice_1 = random.randint(1, 6)
    Dice_2 = random.randint(1, 6)
    if