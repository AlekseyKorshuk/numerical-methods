from dash.dependencies import Input, Output
from methods.euler import EulerMethod
from methods.improved_euler import ImprovedEulerMethod
from methods.runge_kutta import RungeKuttaMethod
from dash import State
import plotly.graph_objects as go
import dash

from controller.base import get_lte_graph, get_gte_graph, get_table, get_methods_graph, \
    get_total_error_over_number_graph
from typing import List, Optional


def import_callbacks(
        app: Optional[dash.Dash]
):
    @app.callback(
        [
            Output(component_id='solutions-graph', component_property='figure'),
            Output(component_id='lte-graph', component_property='figure'),
            Output(component_id='gte-graph', component_property='figure'),
            Output(component_id='total-error-graph', component_property='figure'),
            Output('table', 'figure'),
            Output("loading-output", "children"),
            Output("warning", "is_open"),
        ],
        Input(component_id='initial-x', component_property='value'),
        Input(component_id='final-x', component_property='value'),
        Input(component_id='initial-n', component_property='value'),
        Input(component_id='final-n', component_property='value'),
        Input(component_id='y-function', component_property='value'),
        Input(component_id='y-prime-function', component_property='value'),
        Input(component_id='initial-solution-x', component_property='value'),
        Input(component_id='initial-solution-y', component_property='value'),
        Input(component_id='coefficient-function', component_property='value'),
        # Input("close", "n_clicks"),
        [State("warning", "is_open")],
    )
    def update_output_div(x_0, x_1, n_0, n_1, y_formula, y_prime_formula, x, y, coefficient_formula,
                          is_open) -> Optional[List[dash.dependencies.DashDependency]]:
        """
        Updates all graphs of the app
        :param x_0: Starting point for calculating
        :param x_1: End point for calculating
        :param n_0: Starting grid size for calculating
        :param n_1: End grid size for calculating
        :param y_formula: Formula of y
        :param y_prime_formula: Formula of y'
        :param x: Initial X in IVP
        :param y: Initial Y in IVP
        :param coefficient_index: One of 2 possible coefficients, stars from 1
        :param is_open: State, whether pop-up warning is open
        :return: List of DashDependencies
        """

        x_0 = float(x_0)
        x_1 = float(x_1)
        n_1 = float(n_1)
        n_0 = float(n_0)
        h = (x_1 - x_0) / (n_1 - 1)
        h = float(h)
        x = float(x)
        y_0 = float(y)

        try:
            euler_method = EulerMethod(x_0, x_1, h, y_formula, y_prime_formula, x, y_0, coefficient_formula)
            improved_euler_method = ImprovedEulerMethod(x_0, x_1, h, y_formula, y_prime_formula, x, y_0,
                                                        coefficient_formula)
            rungekutta_method = RungeKuttaMethod(x_0, x_1, h, y_formula, y_prime_formula, x, y_0, coefficient_formula)
            methods = [euler_method, improved_euler_method, rungekutta_method]

            fig = get_methods_graph(methods)
            fig_lte = get_lte_graph(methods)
            fig_gte = get_gte_graph(methods)
            table = get_table(methods)
            total_error_fig = get_total_error_over_number_graph(x_0, x_1, n_0, n_1, y_formula, y_prime_formula, x, y_0,
                                                                coefficient_formula)
        except (ValueError, ZeroDivisionError, IndexError):
            return [go.Figure(), go.Figure(), go.Figure(), go.Figure(), go.Figure(), None, True]
        return [fig, fig_lte, fig_gte, total_error_fig, table, None, False]
