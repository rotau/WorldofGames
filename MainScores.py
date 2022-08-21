from Utils import SCORES_FILE_NAME
from flask import Flask

app = Flask(__name__)


@app.route("/")
def score_server():
    try:
        score_file = open(SCORES_FILE_NAME, 'r', encoding='utf8')
        updated_score = int(score_file.read())
        return f"""<html>
                        <head>
                             <title>Scores Game</title>
                         </head>
                        <body>
                            <h1>The score is <div id="score">{updated_score}</div></h1>
                        </body>
                    </html>"""
    except Exception as error_message:
        return f"""<html>
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                        <body>
                            <h1><div id="score" style="color:red">{error_message}</div></h1>
                        </body>
                    </html>"""


if __name__ == "__main__":
    app.run(debug=True)