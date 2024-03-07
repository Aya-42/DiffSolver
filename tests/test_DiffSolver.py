import numpy as np
import pytest
from DiffSolver import Euler


@pytest.fixture
def exponential_decay_params():
    """Parameters for the exponential decay ODE."""
    k, y0, t0, tf = 1, 1, 0, 10
    return k, y0, t0, tf


def analytical_solution_exponential_decay(t, y0, k):
    return y0 * np.exp(-k * t)


def test_exponential_decay(exponential_decay_params):
    k, y0, t0, tf = exponential_decay_params
    N = 10000
    euler_solver = Euler(f=lambda y, t: -k * y, y0=y0, t0=t0, tf=tf, N=N)
    t, y_numerical = euler_solver.solve()
    y_analytical = analytical_solution_exponential_decay(t, y0, k)

    assert np.allclose(y_numerical, y_analytical,
                       atol=1e-3), "Numerical solution diverges from analytical solution."
