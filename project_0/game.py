'''Guess a number game'''

import numpy as np

number = np.random.randint(1, 101) # guessing a number

# number of attempts
count = 0

while True:
    count+=1
    predict_number = int(input('Guess a number from 1 to 100: '))
    
    if predict_number > number:
        print('The number must be smaller')
        
    elif predict_number < number:
        print('The number must be bigger')
        
    else:
        print(f'You have guessed! The number is {number} for {count} attempts')
        break # end of the game and exit from the loop