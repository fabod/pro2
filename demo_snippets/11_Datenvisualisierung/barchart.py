import plotly.express as px


data = px.data.gapminder()
data_ch = data[data.country == 'Switzerland']
fig = px.bar(data_ch, x='year', y='pop',
             hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
             labels={'pop': 'Einwohner der Schweiz', 'year': 'Jahrzehnt'}, height=400)
fig.show()

# https://plot.ly/python/bar-charts/
