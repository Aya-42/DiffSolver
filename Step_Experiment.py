import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
from DiffSolver import Euler
from numba import vectorize, float64


def analytical_solution(t, y0=1, k=1):
    return y0 * np.exp(-k * t)


def f(y, t):
    k = 1.0  # Example constant, adjust according to your needs
    return -k * y


@vectorize([float64(float64, float64)])
def f_vectorized(y, t):
    k = 1.0  # Example constant, adjust according to your needs
    return -k * y


def compute_error_for_step_size(step_size):
    t0, tf, y0, k = 0, 10, 1, 1
    N = int((tf - t0) / step_size)
    euler_solver = Euler(f=f, y0=y0, t0=t0, tf=tf, N=N)
    t, y_numerical = euler_solver.solve()
    y_analytical = analytical_solution(t, y0, k)
    absolute_error = np.abs(y_numerical - y_analytical)
    relative_error = np.abs((y_numerical - y_analytical) / y_analytical)
    return step_size, t, absolute_error, relative_error


# Assuming f, f_vectorized, and analytical_solution are defined as shown previously

if __name__ == '__main__':
    m_values = range(0, 8)  # Example for step sizes
    step_sizes = [2**-m for m in m_values]

    with Pool(processes=len(step_sizes)) as pool:
        results = pool.map(compute_error_for_step_size, step_sizes)

    # Plot Absolute and Relative Error over Time
    plt.figure(figsize=(14, 6))
    for step_size, t, absolute_error, relative_error in results:
        plt.subplot(1, 2, 1)
        plt.plot(t, absolute_error, label=f'Step size {step_size}')
        plt.subplot(1, 2, 2)
        plt.plot(t, relative_error, label=f'Step size {step_size}')

    plt.subplot(1, 2, 1)
    plt.xlabel('Time')
    plt.ylabel('Absolute Error')
    plt.title('Absolute Error over Time for Different Step Sizes')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.xlabel('Time')
    plt.ylabel('Relative Error')
    plt.title('Relative Error over Time for Different Step Sizes')
    plt.legend()

    plt.tight_layout()
    plt.show()
