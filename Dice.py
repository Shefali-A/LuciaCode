# answer = raw_input("Do you want to roll the dice? ")
# while answer == "y":
#     print randint(1,6)
#     answer = raw_input("Do you want to roll again ")
# print "Goodbye"


# adj = raw_input("Write an adjective? ")
# noun = raw_input("Write a noun? ")
# verb = raw_input("Write a verb? ")
# adverb = raw_input("Write an adverb? ")
# verb2 = raw_input("Write another verb? ")
#
# print "Today I was feeling " + adj + " so I decided to go to the " + noun + \
#       ". I made sure to " + verb + " very " + adverb + " so everyone could " + verb2 + "."

from random import *

def number():
    number = randint(1, 100)
amountOfGuesses = 0
userGuess = None
userGuess = input("Guess a number 1 - 100 ")
i = 0
while i < 10:
    amountOfGuesses = amountOfGuesses + 1
    if userGuess < number:
        print "Your guess is too low."
    if userGuess > number:
        print "Your guess  is too high."
    if userGuess == number:
        print "You are correct!"
    if userGuess != number:
        print "You ran out of guesses. Your number was" + str(number)


    # if amountOfGuesses == 10:
    #     print "You ran out of guesses. Your number was" + str(number)



# 1. define a function
# 2. generate a ramdom number
# 3. create a variable to store the amount of guesses
# 3.5. ask the player to make their guess
# 4. define a while loop (until the person gets the answer right)
# 4.5. keep track of guesses
# 5. write an if statment for conditions (if too high or too low)
# 5.5. after if before while loop ends player must imput answer
# 6. Print out winning statment after completion of while loop

