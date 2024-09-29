'''In this game, there is a list of words present, out of which our interpreter will choose 1 random word. 
The user first has to input their names and then, will be asked to guess any alphabet. 
If the random word contains that alphabet,
it will be shown as the output(with correct placement) 
else the program will ask you to guess another alphabet. 
The user will be given 12 turns(which can be changed accordingly) to guess the complete word.
'''


#  word guessing game
import random
name = input('enter your name')
print('good luck ',name)
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
chance = 12
print(word)
guesses = ""
while chance>0:
    user = input('guess the word: ')
    guesses += user
    for char in word:
        if char in guesses:

            print(char,end=" ")
    else:
        print("_",chance)
        chance-= 1
    if guesses == word:
        print('you WON! \n the word is : ', guesses)
