# Ask the user if they have played before 

show_instructions = ""
while show_instructions.lower() != "xxx":

 show_instructions = input ("Have you played this game before? ").lower()
# If they say yes, output 
if  show_instructions == "yes" or show_instructions == "y":
    print ("program continues")

# if they say no, output 'display instructions'
elif show_instructions == "no" or show_instructions == "n":
    print ("display instructions")

else:
    print ("please answer yes / no") 




# Ask the user if they have played before 

from http.client import responses
from urllib import response


show_instructions = ""
while show_instructions.lower() != "xxx":

show_instructions = input ("Have you played this game before? ").lower()
# If they say yes, output 
if  show_instructions == "yes" or show_instructions == "y":
    print ("program continues")

# if they say no, output 'display instructions'
elif show_instructions == "no" or show_instructions == "n":
    print ("display instructions")

else:
    print ("please answer yes / no") 
def yes_no (question):
valid = False
while not valid:
responses = input ("have you played this game " "before?") . lower()

if response == "yes" or response == "y"
    response = "yes"


elif response == "yes" or response == "n":
    response = "no"  

else:
print ("please answer yes/no")













# Functions go here...



def yes_no(question):

valid = False 

while not valid:

response = input (question).lower()

if response == "yes" or response =="y":

# response ="yes"

return "yes" 


elif response == "no" or response =="n":

response = "no"

return response 

else:     
print ("please answer yes/ no ")



def instructions () :...

def num_check (question, low < high):...

# Main Routine goes here...

played_before = yes_no("have you played the"

" game before? ")

if played_before =="no":   

instructions ()

# Ask user how much they want to play with...

how_much = num_check ("how much would you"

"like to play with? ", 0, 10)

print ("you will be spending ${}".format(how_much))


