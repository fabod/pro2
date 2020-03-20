from flask import Flask
from flask import render_template
from flask import request
import daten

app = Flask("templates")


@app.route("/")
def index():
    return "Willkommen zu unsere App."


@app.route("/speichern/", methods=['GET', 'POST'])
def aktivitaet_speichern():
    if request.method == 'POST':
        aktivitaet = request.form['aktivitaet']
        zeitpunkt, aktivitaet = daten.aktivitaet_speichern(aktivitaet)
        rueckgabe_string = "Gespeichert: " + aktivitaet + " um " + str(zeitpunkt)
        return rueckgabe_string

    return render_template("index.html")


@app.route("/liste")
def auflisten():
    aktivitaeten = daten.aktivitaeten_laden()

    aktivitaeten_liste = ""
    for key, value in aktivitaeten.items():
        zeile = str(key) + ": " + value + "<br>"
        aktivitaeten_liste += zeile

    return aktivitaeten_liste


if __name__ == "__main__":
    app.run(debug=True, port=5000)
