# Ask the user if they have played before 

show_instructions = input ("Have you played this game "
                            "before? ").lower()
# If they say yes, output 
if  show_instructions == "yes":
    print ("program continues")

elif show_instructions == "y":
    print ("program continues")

elif show_instructions == "no":
    print ("display show_instructions")

elif show_instructions == "n":
    print ("display instructions")

# if they say no, output 'display instructions'
print ("please answer yes / no") 