# Functions go here...

# checks for yes / no response
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


# Show instructions
def instructions ():
    print()
    print("Instructions go here")
    return ""

def num_check (question, low, high):
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

played_before = yes_no("have you played the game before? ")

if played_before =="no":   

    instructions ()

how_much = num_check ("how much would you like to play with? ", 0, 10)

print ("you will be spending ${}".format(how_much)) 

# Ask user how much they want to play with...



