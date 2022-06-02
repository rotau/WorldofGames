

def welcome(name):
    print(f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n')


def load_game():
    user_input = True
    second_choice = True
    print('Please choose a game to play:\n',
          '       1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n',
          '       2. Guess Game - guess a number and see if you chose like the computer\n',
          '       3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n')
    while user_input:
        game_selected = input('Please select a game: ')
        if len(game_selected) > 1:
            print('please enter one digit only!')
        elif game_selected.isdigit():
            if int(game_selected) in range(1, 4):
                user_input = False
            else:
                print('Please select option 1, 2 or 3')
        else:
            print('Wrong Value!')
    while second_choice:
        difficulty_level = input('Please choose game difficulty from 1 to 5: ')
        if len(difficulty_level) > 1:
            print('please enter one digit only!')
        elif difficulty_level.isdigit():
            if int(difficulty_level) in range(1, 6):
                second_choice = False
            else:
                print('Please select option 1, 2, 3, 4 or 5')
        else:
            print('Wrong Value!')
    return game_selected, difficulty_level
