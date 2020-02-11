from flask import Flask
from preise import rabatt_berechnen

app = Flask("module")


@app.route("/<preis>")
def rabatt(preis):
    preis_mit_rabatt = rabatt_berechnen(int(preis))

    return "Der neue Preis ist: " + str(preis_mit_rabatt)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
