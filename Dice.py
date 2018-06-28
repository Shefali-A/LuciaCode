from random import *
answer = raw_input("Do you want to roll the dice? ")
while answer == "y":
    print randint(1,6)
    answer = raw_input("Do you want to roll again ")
print "Goodbye"


