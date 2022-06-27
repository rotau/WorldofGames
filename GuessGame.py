import random


def generate_number(difficulty_level):
    secret_number = random.randint(1, difficulty_level + 1)
    return secret_number


def get_guess_from_user(difficulty_level):
    user_input = True
    while user_input:
        number_guessed = input(f'Enter your Guess from 1 to {difficulty_level} : ')
        if len(number_guessed) > 1:
            print('please enter one digit only!')
        elif number_guessed.isdigit():
            if int(number_guessed) in range(1, difficulty_level + 1):
                user_input = False
            else:
                print('Please select option in range')
        else:
            print('Wrong Value!')
    return int(number_guessed)


def compare_results(number_guessed, secret_number ):
    if number_guessed == secret_number:
        result = 'Win'
    else:
        result = "Lose"
    return result


def play(difficulty_level):
    secret_number = generate_number(difficulty_level)
    number_guessed = get_guess_from_user(difficulty_level)
    game_result = compare_results(number_guessed, secret_number )
    if game_result == 'Win':
        game_won = True
    else:
        game_won = False
    return game_won
