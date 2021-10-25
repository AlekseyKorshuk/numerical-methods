from methods.numerical_method import NumericalMethod
from typing import Optional


class EulerMethod(NumericalMethod):
    def __init__(
            self,
            x_0: Optional[float],
            x_1: Optional[float],
            h: Optional[float],
            y_formula: Optional[str],
            y_prime_formula: Optional[str],
            x: Optional[float],
            y: Optional[float],
            coefficient_index: Optional[str]
    ):
        """
        Constructor with parameters
        :param x_0: Starting point for calculating
        :param x_1: End point for calculating
        :param h: Step
        :param y_formula: Formula of y
        :param y_prime_formula: Formula of y'
        :param x: Initial X in IVP
        :param y: Initial Y in IVP
        :param coefficient_index: Formula of C
        """
        super(EulerMethod, self).__init__("Euler", x_0, x_1, h, y_formula, y_prime_formula, x, y, coefficient_index)

    def get_y_method(
            self,
            x: Optional[float],
            y: Optional[float]
    ) -> float:
        """
        Calculates Y using Euler method
        :param x: X value
        :param y: Y value
        :return: Y
        """
        return y + self.h * self.get_y_prime(x, y)
