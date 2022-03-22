import random
from select import select
# Functions go here...
# checks for yes / no response
def yes_no(question):
    valid = False 
    while not valid:
        response = input (question).lower()
        if response == "yes" or response =="y":
            return "yes" 
        elif response == "no" or response =="n":
            return "no" 
        else:     
            print("please answer yes/ no ")
# Show instructions
def instructions():
    print()
    print("Instructions go here")
    print()
  print("select a amount between 1 and 10 and press enter to play if you get A UNICORN you basically win")
    return ""
# checks for numbers between low and high
def num_check(question, low, high):
    error = "please enter an whole number betwwen 1 and 10\n"
    valid = False
    while not valid:
        try:
            # ask the qustion
            response = int (input(question) )
            # if the amount is too low / too high give
            if low < response <= high:
                return response
            # output an error

 else:
                print (error)
        except ValueError:
            print(error)
            # Main Routine goes here...
# decorates statements with symbols above and below
def statement_generator (statement, decoration, style):
    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)
    if style == 3:
        print(top_bottom)
        print(statement)
        print(top_bottom)
    else:
        print(statement)
    return ""
# ****** Main  Routine Starts here *******
statement_generator("Welcome to the Lucky Unicorn Game", '-', 3)
print()
played_before = yes_no("have you played the game before? ")
