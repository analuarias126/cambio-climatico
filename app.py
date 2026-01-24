from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/hola")
def index():
    return render_template("hola.html")


@app.route("/informacion")
def informacion():
    return render_template("infor.html")


@app.route("/analisis")
def analisis():
    return render_template("analisis.html")


@app.route("/lluvia", methods=["GET", "POST"])
def lluvia():
    if request.method == "POST":
        idea = request.form["idea"]

        conn = sqlite3.connect("ideas.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ideas (texto) VALUES (?)", (idea,))
        conn.commit()
        conn.close()

    conn = sqlite3.connect("ideas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ideas")
    ideas = cursor.fetchall()
    conn.close()

    return render_template("lluvia.html", ideas=ideas)


if __name__ == "__main__":
    app.run(debug=True)