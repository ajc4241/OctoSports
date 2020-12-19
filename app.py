from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cyclist")
def cyclist():
    r = random.randint(1, 4)
    return render_template("cyclist.html", rand=r)
@app.route("/football")
def football():
    r = random.randint(1, 4)
    return render_template("football.html", rand=r)
@app.route("/hockey")
def hockey():
    r = random.randint(1, 4)
    return render_template("hockey.html", rand=r)
@app.route("/runner")
def runner():
    r = random.randint(1, 4)
    return render_template("runner.html", rand=r)
@app.route("/bunny")
def bunny():
    r = random.randint(1, 4)
    return render_template("bunny.html", rand=r)
@app.route("/scuba")
def scuba():
    r = random.randint(1, 4)
    return render_template("scuba.html", rand=r)
@app.route("/snowboard")
def snowboard():
    r = random.randint(1, 3)
    return render_template("snowboard.html", rand=r)
@app.route("/soccer")
def soccer():
    r = random.randint(1, 4)
    return render_template("soccer.html", rand=r)
@app.route("/swim")
def swim():
    r = random.randint(1, 4)
    return render_template("swim.html", rand=r)
@app.route("/panda")
def panda():
    r = random.randint(1, 4)
    return render_template("panda.html", rand=r)
if __name__ == "__main__":
    app.run()
