from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife(width=25, height=25)
    return render_template('index.html')


@app.route('/live')
def live():
    game_object = GameOfLife()
    if game_object.counter > 0:
        game_object.form_new_generation()
    game_object.counter += 1
    return render_template('live.html', game_object=game_object)


if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)
