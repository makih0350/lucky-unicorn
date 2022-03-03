from distutils.log import error
from urllib import response


def num_check (question, low, high):
    error = "please enter an whole number betwwen 1 and 10/n"

    valid = False
    while not valid:
        try:
            # ask the qustion 
            response = int (input(question) )
            # if the amount is too low / too high give
            if low < response <= high:
                print ("you have asked to play""with ${}".format (response))

            # output an error
            else:
                print (error)

        except ValueError:
            print(error)


# **** Main Routine goes here ****
how_much = num_check ("how much would you like to play with? ", 0, 10)

print ("you will be spending ${}".format(how_much)) 
#print the
