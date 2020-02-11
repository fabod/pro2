from flask import Flask
from kasse import rabatte
from kasse.rabatte import grosser_rabatt_berechnen

app = Flask("MODULE_2")


@app.route("/<preis>")
def rabatt(preis):
    preis_mit_rabatt = rabatte.rabatt_berechnen(int(preis))

    return "Der neue Preis ist: " + str(preis_mit_rabatt)


@app.route("/grosser_rabatt/<preis>")
def grosser_rabatt(preis):
    preis_mit_rabatt = grosser_rabatt_berechnen(int(preis))

    return "Der neue Preis ist: " + str(preis_mit_rabatt)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
