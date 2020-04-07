from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    name = name.capitalize()
    return render_template("hello.html", name=name)

@app.route("/money", methods=["POST"])
def money():
    amount = request.form.get("amount")
    return render_template("money.html", amount=amount)