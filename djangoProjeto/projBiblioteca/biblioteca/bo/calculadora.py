import plotly.graph_objects as go
import plotly as py

def somar(a, b):
    r = a + b
    return r

def grafico():
    trace = go.Heatmap(z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                       x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                       y=['Morning', 'Afternoon', 'Evening'])
    data=[trace]
    layout = go.Layout(title='Activity Heatmap')

    figure = go.Figure(data=data, layout=layout)

    fig = go.FigureWidget(figure)

    f2 = py.offline.plot(figure, filename='filename.html', auto_open=False)

    return f2

def plotly():

    html = """< div
    id = "82072c0d-ba8d-4e86-b000-0892be065ca8"
    style = "height: 100%; width: 100%;"

    class ="plotly-graph-div" > < / div >

    < script
    type = "text/javascript" > window.PLOTLYENV = window.PLOTLYENV | | {};
    window.PLOTLYENV.BASE_URL = "https://plot.ly";
    Plotly.newPlot("82072c0d-ba8d-4e86-b000-0892be065ca8",
                   [{"y":..bunch of data..., "x":..lots
    of
    data.., {"showlegend": true, "title": "the title", "xaxis": {"zeroline": true, "showline": true},
             "yaxis": {"zeroline": true, "showline": true, "range": [0, 22.63852380952382]}}, {
        "linkText": "Export to plot.ly", "showLink": true}) < / script >"""

    return html




