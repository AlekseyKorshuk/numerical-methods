import dash
from callbacks.source import import_callbacks
from templates.source import layout
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP, 'https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Differential equations | Numerical methods'

server = app.server

app.layout = layout

import_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
