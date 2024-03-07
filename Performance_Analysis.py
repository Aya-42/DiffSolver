import matplotlib.pyplot as plt
import time
import numpy as np
from numba import njit, vectorize

a = -1  # Example value

# ODE: dy/dt = f(t, y) = ay


@njit
def f(t, y):
    return a * y

# Analytical solution for comparison


def analytical_solution(t, y0):
    return y0 * np.exp(a * t)


# Pure Python Implementation
def euler_method(f, y0, t0, tf, dt):
    t = np.arange(t0, tf, dt)
    y = np.empty(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i-1] + f(t[i-1], y[i-1]) * dt
    return t, y


@njit
def euler_method_optimized(f, y0, t0, tf, dt):
    t = np.arange(t0, tf, dt)
    y = np.empty(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i-1] + f(t[i-1], y[i-1]) * dt
    return t, y


# Timing and comparison
y0 = 1
t0 = 0
tf = 5
dt = 0.000001  # Example step size

start_time = time.time()
t_opt, y_opt = euler_method_optimized(f, y0, t0, tf, dt)
optimized_time = time.time() - start_time

start_time = time.time()
t_py, y_py = euler_method(f, y0, t0, tf, dt)
pure_python_time = time.time() - start_time

print(f"Optimized Time: {optimized_time} seconds")
print(f"Pure Python Time: {pure_python_time} seconds")


# step_sizes = np.logspace(-1, -6, num=10)
step_sizes = [5, 3, 2, 1, 0.3, 0.2, 0.1, 0.003, 0.002, 0.001, 0.0003,
              0.0002, 0.0001, 3e-5, 2e-5, 1e-5, 3e-6, 2e-6, 1e-6]  # Example step sizes
errors = []
times = []

for dt in step_sizes:
    start_time = time.time()
    t, y = euler_method_optimized(f, y0, t0, tf, dt)
    total_time = time.time() - start_time
    times.append(total_time)

    y_analytical = analytical_solution(t, y0)
    error = np.abs(y - y_analytical).max()  # Max error
    errors.append(error)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(times, errors, '-o')
plt.xlabel('Computing Time (s)')
plt.ylabel('Error')
plt.title('Error vs. Computing Time for Various Step Sizes')
plt.show()

# Plotting the results
plt.figure(figsize=(10, 6))
plt.loglog(times, errors, '-o')  # Use a log-log plot for better visualization
plt.xlabel('Computing Time (s)')
plt.ylabel('Error')
plt.title('Error vs. Computing Time for Various Step Sizes')
plt.grid(True)
plt.show()
