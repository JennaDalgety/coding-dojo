import random

total_heads = 0
total_tails = 0
count = 0


while count <  5000:

  coin = random.randint(1, 2)

  if coin == 1:
    total_heads += 1
    count += 1

    print "\nAttempt #",count, " throwing a coin...It's a ",coin, "...Got head(s)",total_heads,"times so far and",total_tails,"tail(s) so far."

  elif coin == 2:
    total_tails += 1
    count += 1
 
    print "\nAttempt #",count, "throwing a coin...It's a ",coin, "...Got head(s)",total_heads,"times so far and",total_tails,"tail(s) so far."

print "\nEnding the program, thank you!"