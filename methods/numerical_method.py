import math
import pandas as pd
import numpy as np
from typing import Optional


class NumericalMethod:
    def __init__(
            self,
            title: Optional[str],
            x_0: Optional[float],
            x_1: Optional[float],
            h: Optional[float],
            y_formula: Optional[str],
            y_prime_formula: Optional[str],
            x: Optional[float],
            y: Optional[float],
            coefficient_formula: Optional[str]
    ):
        """
        Constructor with parameters
        :param title: Name of the method
        :param x_0: Starting point for calculating
        :param x_1: End point for calculating
        :param h: Step
        :param y_formula: Formula of y
        :param y_prime_formula: Formula of y'
        :param x: Initial X in IVP
        :param y: Initial Y in IVP
        :param coefficient_formula: Formula of C
        """
        self.title = title
        self.x_0 = x_0
        self.x_1 = x_1
        self.h = h
        self.y_0 = y
        self.dataframe = pd.DataFrame()
        self.y_formula = y_formula
        self.y_prime_formula = y_prime_formula

        self.c = float(eval(coefficient_formula))

        self.calculate()

    def get_y_prime(
            self,
            x: Optional[float],
            y: Optional[float]
    ) -> float:
        """
        Calculates Y'
        :param x: X value
        :param y: Y value
        :return: Y'
        """

        return eval(self.y_prime_formula)

    def get_y(
            self,
            x: Optional[float]
    ) -> float:
        """
        Calculates Y
        :param x: X value
        :return: Y
        """
        return eval(self.y_formula)

    def get_y_method(
            self,
            x: Optional[float],
            y: Optional[float]
    ) -> float:
        """
        Calculates Y using numerical method
        :param x: X value
        :param y: Y value
        :return: Y
        """
        raise NotImplementedError('Subclasses must override get_y_method()!')

    def calculate(self) -> pd.DataFrame:
        """
        Calculates solutions and errors
        :return: Pandas DataFrame with solutions and errors
        """
        x = np.arange(self.x_0, self.x_1 + self.h, self.h)
        y_exact = np.array([self.get_y(i) for i in x])
        y_method = np.zeros(len(x))
        y_method[0] = y_exact[0]
        for i in range(1, len(y_method)):
            y_method[i] = self.get_y_method(x[i - 1], y_method[i - 1])
        GTE = np.zeros(len(x))
        for i in range(len(y_exact)):
            GTE[i] = abs(y_exact[i] - y_method[i])
        LTE = np.zeros(len(x))
        for i in range(1, len(y_exact)):
            LTE[i] = abs(y_exact[i] - self.get_y_method(x[i - 1], y_exact[i - 1]))
        self.dataframe = pd.DataFrame(
            {'X': x, 'Y exact': y_exact, f'Y {self.title}': y_method, f'LTE': LTE, f'GTE': GTE})
        self.dataframe['X'] = self.dataframe['X'].apply(lambda x: round(x, 10))
        return self.dataframe
