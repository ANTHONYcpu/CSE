"""
print("Hello World!")


# This is a comment. This has no effect on the code
# 1. but this does allow me to do things. I can:
# 2. Comment pieces of code that do not work





# 3. Make my code easier to read

print ("There should be a couple blank lines here.")
print ()
print ()
print("There should be a couple blank lines here.")

# Math
print(3 + 5)
print(5 - 2)
print(3 * 4)
print(6 / 2)

print("Figure this out...")
print(6 // 2)
print(5 // 2)
print(9 // 4)

print("Here is another one...")
print(6 % 2)
print(5 % 2)
print(11 % 4)  # Modulus (Remainder)

# Powers
# What is 2^100?
print(2 ** 100)

# Taking input
name = input("What is your name?")
print("Hello %s." % name)

age = input("How old are you? >_")
print("%s?!? You belong in a museum." % age)
print()
print ("%s is really old. They are %s years old." % (name, age))


car_name = "Wiebe Mobile"
car_type = "Tesla"
car_cylinders = 16
car_miles_per_gallon = 0.01

# Make it print "I have a car called Wiebe Mobile. It is a Tesla."


# Recasting
real_age = int (input("How old are you again?") )
hidden_age = real_age + 5
print ("This is your real age:  %d" % hidden_age)
"""



def say_it() :
    print("Hello World!")


say_it()
say_it()
say_it()


#  f(x) =  2x + 3
def f (x):
    print(2*x + 3)


f(1)
f(5)
f(5000)


# Distance Formula
def distance (x1, y1, x2, y2):
     dist = ( (x2-x1) **2 + (y2-y1) **2) ** (1/2)
     print (dist)


distance (0, 0, 3, 4)
distance (0, 0, 5, 12)

# Loops
for i in range(10000):  # This gives the number 0 through 4
    say_it()

    for i in range(1000000):
         print (i + 1)

for i in range(5):
    f (i)

    # white loops