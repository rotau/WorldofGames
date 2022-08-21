import CurrencyRouletteGame
import GuessGame
import MemoryGame
from Scores import add_score


def welcome(name):
    print(f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n')


def input_selection(number_range):
    user_input = True
    while user_input:
        number_selection = input('Enter your choice: ')
        if len(number_selection) > 1:
            print('please enter one digit only!')
        elif number_selection.isdigit():
            if int(number_selection) in range(1, number_range + 1):
                user_input = False
            else:
                print('Please select option 1, 2 or 3')
        else:
            print('Wrong Value!')
    return int(number_selection)


def load_game():
    print('Please choose a game to play:\n',
          '       1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n',
          '       2. Guess Game - guess a number and see if you chose like the computer\n',
          '       3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n')
    game_selected = input_selection(3)
    print('Please choose game difficulty from 1 to 5: \n')
    difficulty_level = input_selection(5)
    if game_selected == 1:
        game_status = MemoryGame.play(difficulty_level)
    elif game_selected == 2:
        game_status = GuessGame.play(difficulty_level)
    elif game_selected == 3:
        game_status = CurrencyRouletteGame.play(difficulty_level)
    if game_status:
        print('Well done! you WIN')
        add_score(difficulty_level)
    else:
        print('Sorry, You LOST!')
