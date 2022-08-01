import random
from time import sleep
from os import system


def screen_cleaner():
    _ = system('clear')


def generate_sequence(difficulty_level):
    random_list = random.sample(range(1, 102), difficulty_level)
    return random_list


def get_list_from_user(difficulty_level):
    user_list = []
    for list_index in range(1, difficulty_level + 1):
        user_input = True
        while user_input:
            number_guessed = input(f'Enter your number {list_index} Guess: ')
            if len(number_guessed) > 3:
                print('please enter  digits in the range 1-102!')
            elif number_guessed.isdigit():
                if int(number_guessed) in range(1, 103):
                    user_input = False
                else:
                    print('Please select option in range')
            else:
                print('Wrong Value!')
        user_list.append(int(number_guessed))
    return user_list


def is_list_equal(user_list, random_list):
    return user_list == random_list


def play(difficulty_level):
    random_list = generate_sequence(difficulty_level)
    print('Can you remember the numbers?\n', random_list)
    sleep(2)
    screen_cleaner()
    user_list = get_list_from_user(difficulty_level)
    game_result = is_list_equal(user_list, random_list)
    return game_result
