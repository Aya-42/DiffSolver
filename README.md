# Overview

This repo is part of an assignment for the HPC course at UTD. This assignment involves implementing the Euler method to solve a specific ODE, exploring the effects of step size on the solution’s accuracy, and optimizing the implementation for performance using Python’s advanced numerical and parallel computing libraries.


## Repository Structure
- `DiffSolver.py`: The core class encapsulating the Euler method. It has the potential to exapnd to other methods, as it is a superclass. I wanted it to include optimized Numba implmentation but failed due to NUMBA limitation.
- `DiffSolver_simple_tests.py`: Contains 2 unit tests for `DiffSolver.py` to validate the correctness of the Euler method implementation against known solutions.
- `Step_Experiment.py`: A script to conduct experiments with various step sizes and analyze their impact on the accuracy of the differential equation solutions.
- `Performance_Analysis.py`: A Script dedicated to analyzing and comparing the performance of the optimized Euler method against the non-optimized version.
- `requirements.txt`: A list of Python dependencies necessary to run the project.

## Installing dependancies
```bash
pip install -r requirements.txt
