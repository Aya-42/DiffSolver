# Euler Method: Analysis Report

## Overview

[GitHub - Aya-42/DiffSolver](https://github.com/Aya-42/DiffSolver)

## Results and Discussion

### Euler Step Tests

---

The provided Python script includes two test functions intended to validate the accuracy and functionality of the Euler based differential equation solver. Below is a documentation of the tests and their coverage:

### `test_exponential_decay`

This test verifies the solver's ability to accurately approximate the solution to an exponential decay problem.

$$
\frac{dy}{dt}
= -ky
$$

The analytical solution for this equation, given initial condition $y(0) = y_0$, is $y(t) = y_0 e^{-kt}$. The test uses the `Euler` class to numerically solve the ODE over a time range from `t0` to `tf` with a total of `N` steps. It then compares the numerical solution to the analytical solution using `np.allclose` with an absolute tolerance of `1e-3`, asserting that the two solutions should be nearly identical within this tolerance. Besides the assertion, the test plots both the numerical and analytical solutions for visual inspection, aiding in qualitative analysis of the Euler method's performance.

<img title="" src="file:///D:/Google%20Drive/DiffSolver/Figure_1.png" alt="Untitled" data-align="center" width="509">

### `test_linear_growth`

- This test checks the solver's capability to accurately simulate linear growth $\frac{dy}{dt} =2t$ which has an analytical solution $y(t) = t^2 + C$.Similarly, this function employs the `Euler` class to compute the numerical solution over a specified interval and number of steps. It then asserts that the numerical solution approximates the analytical solution within an absolute tolerance of `1e-1`, again utilizing `np.allclose` for the comparison. The test also plots the numerical solution against the analytical solution, providing a visual comparison to assess the accuracy of the numerical method.

<img title="" src="file:///D:/Google%20Drive/DiffSolver/Figure_2.png" alt="Untitled" data-align="center" width="503">

#### Usage with pytest

To run these tests using pytest, ensure the test functions are saved in a Python file, e.g., `test_diffsolver.py`. Then, in the terminal, navigate to the directory containing the test file and execute:

```bash
pytest test_diffsolver.py
```

Pytest will automatically discover and run the tests, reporting their success or failure based on the assertions within each test
function. I made two copies of the same test, one in a file that pytest can recognize and one is not, and is just for the purpose of quick local testing and generating plots. I am sure there is a better way to implement this, but I ran out of time.

### Step Size

---

To infer the relation between error and step size, the ODE for exponential decay is solved numerically over a range of step sizes. The figures show plots of absolute and relative errors over time for various step sizes.

![Untitled](D:\Google%20Drive\DiffSolver\Figure_3.png)

It is clear from the plots that that reducing the step size in Euler's method improves the accuracy of the solution, as evidenced by a decrease in error. Nevertheless, there comes a point where making the step size even smaller yields negligible improvements in precision, which may not be cost-effective considering the increased computational demand.

### Performance

After testing is verified, the profiling process was done using py-spy to pinpoint performance bottlenecks. flame graphs pre- and post-compilation of NUMBA is shown in the figure below. A quick analysis of the post-compilation flame graphs pinpointed the for loop, where the Euler method execution happens, as the primary area where execution time was concentrated. This is expected, but it is further indication to add in the NUMBA optimization to that specific part of the code.

| <img title="" src="file:///D:/Google%20Drive/DiffSolver/svgtopng/profile.png" alt="Untitled" data-align="inline" width="1095"> | <img title="" src="file:///D:/Google%20Drive/DiffSolver/svgtopng/profile2.png" alt="Untitled" data-align="inline" width="1111"> |
| ------------------------------------------------------------------------------------------------------------------------------ |:-------------------------------------------------------------------------------------------------------------------------------:|

For a large step size, the optimized implementation shown much larger time than the pure one. But, as step size is adjusted, both accuracy and the efficacy of parallelization improved. For a step size of dt = 0.000001 seconds the optimized time vs the pure one was (1.1298 seconds, 4.214 seconds). The figure below is before optimization.

<img title="" src="file:///D:/Google%20Drive/DiffSolver/Figure_5.png" alt="Untitled" data-align="center" width="518">

The effect of the optimization is evident by figure below, compared to the above figure, the result is more accurate and faster with the same resources.

<img title="" src="file:///D:/Google%20Drive/DiffSolver/Figure_4.png" alt="Untitled" width="528" data-align="center">

## Conclusions

- There is an optimal step size that balances accuracy with computational efficiency.
- overhead for NUMBA optimization is noticeable at large step sizes but it is not for small ones.
- The optimization efforts have a notable effect on performance. Although there is an initial cost in compiling the optimized code, the subsequent execution is much faster compared to the pure Python implementation, and thus we are able to reach the same accuracy with much fewer resources.
- While optimization significantly improves computational performance, careful consideration must be given to selecting an appropriate step size that balances computational efficiency with the desired accuracy of the numerical solution.
