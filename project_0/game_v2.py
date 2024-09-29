'''Guess a number game
Our computer makes a wish and try to guess it on its own
'''

import numpy as np

def random_predict(number: int=1) -> int:
    """Guessing a number randomly

    Args:
        number (int, optional): wished number. Defaults to 1.

    Returns:
        int: number of attempts
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break # exit from the loop, if the number was guessed
        
    return(count)

def score_game(random_predict) -> int:
    """How many attempts on average does our computer to guess the number per 1000

    Args:
        random_predict (_type_): function of guessing

    Returns:
        int: average number of attempts
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size = (1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Our algoritm guesses the number average for {score} attempts')
    return(score)

if __name__ == '__main__':

    score_game(random_predict)
