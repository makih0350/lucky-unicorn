# Ask the user if they have played before 
show_instructions = input ("Have you played this game before? ").lower()
# if they say yes, output 'program continues'  
if show_instructions == "yes": 
    print ("program continues")
# if they say no, output 'display instructions' 
elif show_instructions == "no": 
    print ("display instructions")
else:
    print ("please answer yes / no")
    



   #  count up from one to 10...

for item in range (1, 10):
    print (item)
