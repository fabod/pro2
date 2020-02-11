from flask import Flask
import preise

app = Flask("module")


@app.route("/<preis>")
def rabatt(preis):
    preis_mit_rabatt = preise.rabatt_berechnen(int(preis))

    return "Der neue Preis ist: " + str(preis_mit_rabatt)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
