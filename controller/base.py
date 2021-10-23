import plotly.graph_objects as go
import pandas as pd
import numpy as np
from methods.euler import EulerMethod
from methods.improved_euler import ImprovedEulerMethod
from methods.runge_kutta import RungeKuttaMethod
from methods.numerical_method import NumericalMethod
from typing import List, Optional


def get_methods_graph(
        methods: Optional[List[NumericalMethod]]
) -> go.Figure():
    """
    Returns the graph of exact and numerical solutions
    :param methods: List of methods to plot graph with
    :return: Resulting figure
    """
    fig = go.Figure()

    fig.add_trace(
        go.Line(
            x=methods[0].dataframe['X'],
            y=methods[0].dataframe[f'Y exact'],
            name='Exact'
        )
    )

    for method in methods:
        fig.add_trace(
            go.Line(
                x=method.dataframe['X'],
                y=method.dataframe[f'Y {method.title}'],
                name=method.title
            )
        )

    fig.update_layout(
        title={
            'text': 'The graph of exact and numerical solutions',
            'xanchor': 'center',
            'yanchor': 'top',
            'y': 0.9,
            'x': 0.5,
        },
        yaxis=dict(
            title="Y",
        ),
        xaxis=dict(
            title="X",
        ),
    )

    return fig


def get_lte_graph(
        methods: Optional[List[NumericalMethod]]
) -> go.Figure():
    """
    Returns the graph of local truncation error
    :param methods: List of methods to plot graph with
    :return: Resulting figure
    """
    fig = go.Figure()

    for method in methods:
        fig.add_trace(
            go.Line(
                x=method.dataframe['X'],
                y=method.dataframe['LTE'],
                name=method.title
            )
        )

    fig.update_layout(
        title={
            'text': 'The graph of local truncation errors',
            'xanchor': 'center',
            'yanchor': 'top',
            'y': 0.9,
            'x': 0.5,
        },
        yaxis=dict(
            title="LTE",
        ),
        xaxis=dict(
            title="X",
        ),
    )

    return fig


def get_gte_graph(
        methods: Optional[List[NumericalMethod]]
) -> go.Figure():
    """
    Returns the graph of global truncation error
    :param methods: List of methods to plot graph with
    :return: Resulting figure
    """
    fig = go.Figure()

    for method in methods:
        fig.add_trace(
            go.Line(
                x=method.dataframe['X'],
                y=method.dataframe['GTE'],
                name=method.title
            )
        )

    fig.update_layout(
        title={
            'text': 'The graph of global truncation errors',
            'xanchor': 'center',
            'yanchor': 'top',
            'y': 0.9,
            'x': 0.5,
        },
        yaxis=dict(
            title="GTE",
        ),
        xaxis=dict(
            title="X",
        ),
    )

    return fig


def get_table(
        methods: Optional[List[NumericalMethod]]
) -> go.Figure():
    """
    Returns the table with all solutions end errors
    :param methods: List of methods to plot graph with
    :return: Resulting figure
    """
    header = []
    values = []
    for method in methods:
        columns = list(method.dataframe.columns)
        if 'X' in header:
            columns.remove('X')
        if 'Y exact' in header:
            columns.remove('Y exact')
        for column in columns:
            values.append(method.dataframe[column].tolist())

        columns[columns.index('LTE')] = f'LTE {method.title}'
        columns[columns.index('GTE')] = f'GTE {method.title}'

        header += list(columns)

    table = pd.DataFrame()
    table[0] = values[0]
    for i in range(1, len(header)):
        if 'TE' in header[i]:
            table[header[i]] = values[i]
    # table.to_csv("dataframe-errors.csv")

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(header),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(
            values=values,
            align="left")
    )
    ])

    fig.update_layout(
        title={
            'text': 'Table',
            'xanchor': 'center',
            'yanchor': 'top',
            'y': 0.9,
            'x': 0.5,
        },
    )

    return fig


def get_total_error_over_number_graph(
        x_0: Optional[float],
        x_1: Optional[float],
        n_0: Optional[float],
        n: Optional[float],
        y_formula: Optional[str],
        y_prime_formula: Optional[str],
        x: Optional[float],
        y_0: Optional[float],
        coefficient_index: Optional[int]

) -> go.Figure():
    """
    Returns the graph of total approximation error depending on the number of grid cells
    :param x_0: Starting point for calculating
    :param x_1: End point for calculating
    :param n_0: Starting grid size for calculating
    :param n: End grid size for calculating
    :param y_formula: Formula of y
    :param y_prime_formula: Formula of y'
    :param x: Initial X in IVP
    :param y_0: Initial Y in IVP
    :param coefficient_index: One of 2 possible coefficients, stars from 1
    :return: Resulting figure
    """
    fig = go.Figure()

    gte_number_dataset = pd.DataFrame()
    gte_number_dataset['N'] = range(int(n_0), int(n) + 1, 1)
    gte_number_dataset['Euler'] = np.zeros(int(n) - int(n_0) + 1)
    gte_number_dataset['Improved Euler'] = np.zeros(int(n) - int(n_0) + 1)
    gte_number_dataset['Runge-Kutta'] = np.zeros(int(n) - int(n_0) + 1)

    methods = []
    for n in gte_number_dataset['N']:
        euler_method = EulerMethod(x_0, x_1, (x_1 - x_0) / n, y_formula, y_prime_formula, x, y_0, coefficient_index)
        improved_euler_method = ImprovedEulerMethod(x_0, x_1, (x_1 - x_0) / n, y_formula, y_prime_formula, x, y_0,
                                                    coefficient_index)
        rungekutta_method = RungeKuttaMethod(x_0, x_1, (x_1 - x_0) / n, y_formula, y_prime_formula, x, y_0,
                                             coefficient_index)
        methods = [euler_method, improved_euler_method, rungekutta_method]
        for method in methods:
            # print(max(method.dataframe['LTE']))
            gte_number_dataset[method.title][n - int(n_0)] = max(method.dataframe['GTE'])

    # gte_number_dataset.to_csv('total-errors.csv')
    for method in methods:
        fig.add_trace(
            go.Line(
                x=gte_number_dataset['N'],
                y=gte_number_dataset[method.title],
                name=method.title
            )
        )

    fig.update_layout(
        title={
            'text': 'The graph of total errors over N',
            'xanchor': 'center',
            'yanchor': 'top',
            'y': 0.9,
            'x': 0.5,
        },
        yaxis=dict(
            title="Total error",
        ),
        xaxis=dict(
            title="N",
        ),
    )

    return fig
