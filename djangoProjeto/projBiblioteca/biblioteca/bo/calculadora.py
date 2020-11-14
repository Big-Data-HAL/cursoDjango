import plotly.graph_objects as go

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

    f2 = go.FigureWidget(figure)

    return f2