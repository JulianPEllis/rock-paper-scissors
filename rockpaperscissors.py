import random
import array

choices = ['Rock', 'Paper', 'Scissors']

def choose():

    if userInput == output:
       print('It\'s a draw!')



    if userInput == 'Rock':
        if output == 'Scissors':
            print('You Win!')



    if userInput == 'Rock':
        if output == 'Paper':
            print('You Lose!')



    if userInput == 'Paper':
        if output == 'Rock':
            print('You Win!')



    if userInput == 'Paper':
        if output == 'Scissors':
            print('You Lose!')



    if userInput == 'Scissors':
        if output == 'Rock':
            print('You Lose!')



    if userInput == 'Scissors':
        if output == 'Paper':
            print('You Win!')


while True:

    userInput = input('> ') # Input Variable

    if userInput == 'Rock':
        output = random.choice(choices)
        print(output)
        choose()

    if userInput == 'Paper':
        output = random.choice(choices)
        print(output)
        choose()

    if userInput == 'Scissors':
        output = random.choice(choices)
        print(output)
        choose()