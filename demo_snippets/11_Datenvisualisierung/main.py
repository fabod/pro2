from flask import Flask
from flask import render_template

import plotly.express as px
from plotly.offline import plot

app = Flask("Datenvisualisierung")


def data():
    data = px.data.gapminder()
    data_ch = data[data.country == 'Switzerland']

    return data_ch


def viz():
    data_ch = data()

    fig = px.bar(
        data_ch,
        x='year', y='pop',
        hover_data=['lifeExp', 'gdpPercap'],
        color='lifeExp',
        labels={
            'pop': 'Einwohner der Schweiz',
            'year': 'Jahrzehnt'
        },
        height=400
    )

    div = plot(fig, output_type="div")
    return div


@app.route("/")
def index():
    div = viz()
    # return str([str(i) for i in data()])
    return render_template('index.html', viz_div=div)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
