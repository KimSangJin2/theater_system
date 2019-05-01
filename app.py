from flask import Flask, render_template
from scheduler import movie_list, schedule_list

app = Flask(__name__)

movieManager = schedule_list()
movies = movieManager.get_schedule()


@app.route("/")             #헬로 함수에 라우트라는 기능을 주는 것. 125.1.1.1/  '/'라는 곳에 들어간거야.
def hello():
    return render_template("test.html", name='김상진', movies = movies)


app.run()