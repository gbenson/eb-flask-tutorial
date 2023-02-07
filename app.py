from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hello.html")

@app.route("/<username>")
def hello(username):
    return render_template("hello.html", username=username)

if __name__ == "__main__":
    print('Try "flask --debug run".')
