
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


# **** Main Routine goes here ****

# Ask the user if they have played before 
# show_instructions = input ("Have you played this game "
#                             "before? ").lower()
# If they say yes, output 'program continues

how_much = num_check ("how much would you like to play with? ", 0, 10)

print ("you will be spending ${}".format(how_much)) 
#print the
