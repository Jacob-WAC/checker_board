from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def placeholder():
    return render_template("index.html", xtimes=8, ytimes=8, color1="black", color2="red")


@app.route('/<xtimes>')
def placeholder2(xtimes):
    return render_template("index.html", xtimes=int(xtimes), ytimes=int(xtimes), color1="black", color2="red")


@app.route('/<xtimes>/<ytimes>')
def placeholder3(xtimes, ytimes):
    return render_template("index.html", xtimes=int(xtimes), ytimes=int(ytimes), color1="black", color2="red")


@app.route('/<xtimes>/<ytimes>/<color1>/<color2>')
def placeholder4(xtimes, ytimes, color1="black", color2="red"):
    return render_template("index.html", xtimes=int(xtimes), ytimes=int(ytimes), color1=color1, color2=color2)


@app.errorhandler(404)
def error(error):
    return "Sorry! No response. Try again"


if __name__ == "__main__":
    app.run(debug=True)
