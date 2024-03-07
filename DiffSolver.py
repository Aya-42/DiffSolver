from numba import jit
from typing import Callable, Tuple
import numpy as np


class DiffSolver:
    def __init__(
        self,
        f: Callable[[float, float], float],
        y0: float,
        t0: float,
        tf: float,
        N: int,
    ):
        """
        Initializes the ODE solver with a given differential equation, initial conditions, and time span.

        Parameters:
        - f: The driving function of the ODE, f(x, t).
        - y0: Initial condition of the ODE.
        - t0: Start time of the simulation.
        - tf: End time of the simulation.
        - N: Number of steps to take in the simulation.
        """
        if tf <= t0:
            raise ValueError("End time tf must be greater than start time t0.")
        if N <= 0:
            raise ValueError("Number of steps N must be positive.")
        self.f = f
        self.y0 = y0
        self.t = np.linspace(t0, tf, N + 1)

    @property
    def step_size(self) -> float:
        return (self.t[-1] - self.t[0]) / self.N

    def solve(self) -> Tuple[np.ndarray, np.ndarray]:
        """Placeholder method for solving the ODE. Must be implemented by subclasses."""
        raise NotImplementedError(
            "Solve method must be implemented by specfic subclass."
        )

    def __str__(self) -> str:
        t, y = self.solve()
        return f"Time points: {t}\nSolution values: {y}"


class Euler(DiffSolver):
    """
    A class that implements the Euler method for solving differential equations.
    """

    def solve(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Solves the differential equation using the Euler method. Overides methods from superclass when called.

        Returns:
            A tuple containing two numpy arrays: the time values and the corresponding solution values.
        """
        y = np.zeros(len(self.t))
        y[0] = self.y0

        for i in range(1, len(self.t)):
            dt = self.t[i] - self.t[i - 1]
            y[i] = y[i - 1] + dt * self.f(y[i - 1], self.t[i - 1])
        return self.t, y

    # @staticmethod
    # @jit(nopython=True)
    # def _solve_jit(t: np.ndarray, y: np.ndarray, y0: float, f: Callable[[float, float], float]) -> np.ndarray:
    #     """
    #     Static method that performs the Euler method calculations.
    #     This method is JIT-compiled for performance.

    #     Parameters:
    #         t (np.ndarray): Array of time points.
    #         y (np.ndarray): Array to store the solution.
    #         y0 (float): Initial condition of the ODE.
    #         f (Callable): The driving function of the ODE, f(y, t).

        # Returns:
    #         np.ndarray: The solution array after applying the Euler method.
    #     """
    #     for i in range(1, len(t)):
    #         dt = t[i] - t[i - 1]
    #         y[i] = y[i - 1] + dt * f(y[i - 1], t[i - 1])
    #     return y
