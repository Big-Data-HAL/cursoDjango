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

    html = """<table style="width:100%">
              <tr>
                <th>Firstname</th>
                <th>Lastname</th>
                <th>Age</th>
              </tr>
              <tr>
                <td>Jill</td>
                <td>Smith</td>
                <td>50</td>
              </tr>
              <tr>
                <td>Eve</td>
                <td>Jackson</td>
                <td>94</td>
              </tr>
              </table>"""

    return html




