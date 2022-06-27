import requests
import json
import random


def get_money_interval(difficulty_level):
    url = "https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=93e8d1006c63e39755e7"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    api_data = json.loads(response.text)
    currency_rate = api_data['USD_ILS']
    currency_interval_low = currency_rate - (5 - difficulty_level)
    currency_interval_high = currency_rate + (5 - difficulty_level)
    return currency_interval_low, currency_interval_high


def get_guess_from_user(guess_interval_high, game_money_sum):
    user_input = True
    while user_input:
        number_guessed = input(f'Enter your Guess for the value of {game_money_sum}: ')
        if number_guessed.isdigit():
            user_input = False
        else:
            print('Wrong Value!')
    return float(number_guessed)


def play(difficulty_level):
    game_money_sum = random.randint(1, 100)
    currency_interval_low, currency_interval_high = get_money_interval(difficulty_level)
    guess_interval_low = currency_interval_low * game_money_sum
    guess_interval_high = currency_interval_high * game_money_sum
    user_guess = get_guess_from_user(guess_interval_high, game_money_sum)
    return user_guess > guess_interval_low and user_guess < guess_interval_high
