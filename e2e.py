from selenium import webdriver
import sys


def test_scores_service():
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:5000')
    score_value = driver.find_element('xpath', '//*[@id="score"]')
    score = score_value.text
    if int(score) > 1 and int(score) < 1000:
        return True
    else:
        return False


def main_function():
    if test_scores_service():
        return sys.exit(0)
    else:
        return sys.exit(1)
