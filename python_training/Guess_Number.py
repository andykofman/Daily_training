## 2. Guess the Number
# Write a number-guessing game:
# 
# Generate a random number between 1 and 100.
# 
# Let the user guess until they find the number.
# 
# Tell them if each guess is too high or too low.
# 
# After they guess correctly, print how many attempts they took.
# 
# (Apply: loops, functions, input, random module)

import random
import math

guess = random.randint(1,100)
attempts=[]
while True:
    try: 

        user_input = int(input('Please guess a number from 1 to 100\n'))
        attempts.append(user_input)
        count = 0
        for i in attempts:

            count = count +1
            
        if guess == user_input:
            print ('Bingo')
            print (count)
            break
        elif guess > user_input: 
            print('Go a little bit higher')
        else:
            print('Go a little lower')
    except ValueError: 
            print ('Enter Numbers only')

print('Thank You for playing')
