from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cyclist")
def cyclist():
    return render_template("cyclist.html")
if __name__ == "__main__":
    app.run()
