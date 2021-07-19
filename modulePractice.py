import random
# or you could do 
# from random import *

# if you do that you don't need to specify random.me
# but the code is less readable

# Loc 9% thru book
while True: #repeats over and over until it breaks
    randomNumber = random.randint(5, 20)
    if randomNumber != 13: 
        print(randomNumber)
        continue #practice w continue
    elif randomNumber == randomNumber:
        print("Your number is 13!")
        break # practice with break
    print("This should never print.")