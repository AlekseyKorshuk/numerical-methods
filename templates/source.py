from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

# Dash layout of the app
layout = html.Div([
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Warning!", style={"fontSize": 32, "fontWeight": "bold"})),
            dbc.ModalBody("Current inputs are out of the domain."),
            dbc.ModalBody("Please change your input parameters."),
            # dbc.ModalFooter(
            #     dbc.Button(
            #         "Close", id="close", className="ms-auto", n_clicks=0
            #     )
            # ),
        ],
        id="warning",
        is_open=False,
    ),
    html.Div(
        [
            html.H3("Differential equations | Numerical methods"),
        ], style={'display': 'inline-block', 'width': '100%', 'text-align': 'center'}
    ),
    html.Div(
        [
            "Formula of y:",
            html.Br(),
            dcc.Input(id='y-function', value='x*(-2/math.sqrt(x)/self.c + 1/x/self.c/self.c + 2)', type='text'),
            html.Br(),
            "Formula of y':",
            html.Br(),
            dcc.Input(id="y-prime-function", value='(y - x)**0.5 / x**0.5 + 1', type='text'),
            html.Br(),
            "Formula of coefficient:",
            html.Br(),
            dcc.Input(id="coefficient-function", value='(-1 * math.sqrt(x) - math.sqrt(y - x)) / (y - 2 * x)',
                      type='text'),
            html.Br(),

        ],
        style={'display': 'inline-block', 'width': '100%', 'padding': '0px 44%'}
    ),

    html.Div(
        [
            "Starting point:",
            html.Br(),
            dcc.Input(id='initial-x', value='1', type='number'),
            html.Br(),
            "End point:",
            html.Br(),
            dcc.Input(id='final-x', value='15', type='number'),
            html.Br(),
            "Initial X:",
            html.Br(),
            dcc.Input(id='initial-solution-x', value='1', type='number'),
            html.Br(),
            "Initial Y:",
            html.Br(),
            dcc.Input(id='initial-solution-y', value='10', type='number'),
            html.Br(),
            "Starting number of points:?????????",
            html.Br(),
            dcc.Input(id='initial-n', value='2', type='number', step=1),
            html.Br(),
            "End number of points:?????????",
            html.Br(),
            dcc.Input(id='final-n', value='15', type='number', step=1),

        ],
        style={'display': 'inline-block', 'width': '100%', 'padding': '0px 44%'}
    ),
    html.Br(),
    html.Br(),
    dcc.Loading(
        id="loading",
        type="circle",
        children=html.Div(id="loading-output"),
        style={"visibility": "visible !important"}
    ),
    html.Br(),

    html.Div(
        [
            dcc.Graph(id='solutions-graph')
        ], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}
    ),
    html.Div(
        [
            dcc.Graph(id='lte-graph'),
        ], style={'display': 'inline-block', 'width': '49%', 'padding': '0 20'}
    ),
    html.Div(
        [
            dcc.Graph(id='gte-graph'),
        ], style={'display': 'inline-block', 'width': '49%'}
    ),
    html.Div(
        [
            dcc.Graph(id='total-error-graph')
        ], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}
    ),
    html.Br(),
    html.Div(
        dcc.Graph(id='table')
        # html.Iframe(id = 'table', height=500, width="100%", style={'frameBorder':"0"})
    ),
    html.Footer(
        [
            dcc.Markdown("**Created by [Aleksey Korshuk](https://github.com/AlekseyKorshuk)**"),
            dcc.Markdown(
                "[![Follow](https://img.shields.io/github/followers/AlekseyKorshuk?style=social)](https://github.com/AlekseyKorshuk)"),
            dcc.Markdown(
                "[![GitHub stars](https://img.shields.io/github/stars/AlekseyKorshuk/numerical-methods?style=social)](https://github.com/AlekseyKorshuk/numerical-methods)"
            ),

        ],
        style={'display': 'inline-block', 'width': '100%', 'text-align': 'center'}
    ),
    html.Br(),
    html.Br(),
    html.Br(),

])
