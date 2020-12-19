from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cyclist")
def cyclist():
    return render_template("cyclist.html")
@app.route("/football")
def football():
    return render_template("football.html")
@app.route("/hockey")
def hockey():
    return render_template("hockey.html")
@app.route("/runner")
def runner():
    return render_template("runner.html")
@app.route("/bunny")
def bunny():
    return render_template("bunny.html")
@app.route("/scuba")
def scuba():
    return render_template("scuba.html")
@app.route("/snowboard")
def snowboard():
    return render_template("snowboard.html")
@app.route("/soccer")
def soccer():
    return render_template("soccer.html")
@app.route("/swim")
def swim():
    return render_template("swim.html")
@app.route("/panda")
def panda():
    return render_template("panda.html")
if __name__ == "__main__":
    app.run()
