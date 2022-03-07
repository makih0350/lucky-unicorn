# testing loop to generate 20 tokens
for item in range (0,20):
    chosen = randon.choice (tokens)
  
  # adjust balace
  if chosen == "unicorn":
      balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

        # output
        print 