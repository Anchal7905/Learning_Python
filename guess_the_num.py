# number guessing game in python
# NOTE :Minimum number of guessing = log2(Upper bound – lower bound + 1)
import random
import math
lower = int(input('enter the lower range:'))
upper = int(input('enter the upper range:'))
comp = random.randrange(lower,upper)
user = 0
print("\n\tYou've only ", 
       round(math.log(upper - lower + 1, 2)),
       "to guess the number!!")
n = 1
while(n<math.log(upper - lower + 1, 2) ):
    user = int(input('enter your guess number:'))
    if user == comp:
        print('congratulations!, You gussed the number correctly')
        break
    if user> comp:
        print('Try Again! You guessed too high')
    if user< comp:
        print('Try Again! You guessed too low')
    n = n +1
print('Total Number of Guesses =',n)
if n>math.log(upper - lower + 1, 2):
    print("!!Better luck next time!!")
    print('random number is:', comp)