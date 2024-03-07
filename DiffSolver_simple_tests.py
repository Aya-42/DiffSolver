import numpy as np
import matplotlib.pyplot as plt

from DiffSolver import Euler


def analytical_solution(t, y0=1, k=1):
    return y0 * np.exp(-k * t)


def test_exponential_decay():
    k, y0, t0, tf, N = 1, 1, 0, 10, 10000
    euler_solver = Euler(f=lambda y, t: -k * y, y0=y0, t0=t0, tf=tf, N=N)
    t, y_numerical = euler_solver.solve()
    y_analytical = analytical_solution(t, y0, k)

    # Compare numerical and analytical solutions
    assert np.allclose(
        y_numerical, y_analytical, atol=1e-3
    ), "Numerical solution for exponential_decay diverges from analytical solution."

    # Plot for visual comparison
    plt.figure(figsize=(10, 6))
    plt.plot(t, y_numerical, label="Numerical - Euler")
    plt.plot(t, y_analytical, "k--", label="Analytical")
    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("y")
    plt.title("Exponential Decay: Numerical vs Analytical Solution")
    plt.grid(True)
    plt.show()


def test_linear_growth():
    # ODE: dy/dt = 2t, with analytical solution y(t) = t^2 + C
    y0, t0, tf, N = 0, 0, 5, 1000  # Let C=y0=0 for simplicity
    euler_solver = Euler(f=lambda y, t: 2 * t, y0=y0, t0=t0, tf=tf, N=N)
    t, y_numerical = euler_solver.solve()
    y_analytical = t**2

    # Assert close approximation between numerical and analytical solutions
    assert np.allclose(
        y_numerical, y_analytical, atol=1e-1
    ), "Numerical solution for linear growth diverges from analytical solution."

    # Plot for visual comparison
    plt.figure(figsize=(10, 6))
    plt.plot(t, y_numerical, label="Numerical - Euler")
    plt.plot(t, y_analytical, "k--", label="Analytical - Linear Growth")
    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("y")
    plt.title("Linear Growth: Numerical vs Analytical Solution")
    plt.grid(True)
    plt.show()


# If using pytest, the assertion will automatically trigger the test fail/pass.
# For manual execution, simply call the function
test_exponential_decay()
test_linear_growth()
