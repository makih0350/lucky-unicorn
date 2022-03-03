# Functions go here...



def yes_no(question):

    valid = False 

    while not valid:

        response = input (question).lower()

        if response == "yes" or response =="y":
            return "yes" 

        elif response == "no" or response =="n":
            return response 

        else:     
            print ("please answer yes/ no ")



def instructions ():
    print()
    print("Instructions go here")
    return ""

def num_check (question, low, high):...

# Main Routine goes here...

played_before = yes_no("have you played the game before? ")

if played_before =="no":   

    instructions ()

# Ask user how much they want to play with...



