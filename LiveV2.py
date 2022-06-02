
def welcome(name):
    print(f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n')


def load_game():
    game_selected = ' '
    difficulty_selected = ' '
    print('Please choose a game to play:\n',
          '       1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n',
          '       2. Guess Game - guess a number and see if you chose like the computer\n',
          '       3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n')
    while game_selected not in ['1', '2', '3']:
        game_selected = input('Please select a game: ')

    while difficulty_selected not in ['1', '2', '3', '4', '5']:
        difficulty_selected = input('Please choose game difficulty from 1 to 5: ')

    return game_selected, difficulty_selected
