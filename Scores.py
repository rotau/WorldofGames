from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    try:
        score_file = open(SCORES_FILE_NAME, 'r', encoding='utf8')
    except:
        score_file = open(SCORES_FILE_NAME, 'w')
        score_file.write('0')
        score_file = open(SCORES_FILE_NAME, 'r', encoding='utf8')
    score_file.seek(0)
    point_of_winning = (difficulty * 3) + 5
    updated_score = point_of_winning + int(score_file.read())
    score_file = open(SCORES_FILE_NAME, 'w')
    score_file.write(str(updated_score))
    score_file.close()
