# import time
# import matplotlib.pyplot as plt
# from numpy.polynomial import Polynomial as P
from random import shuffle


def function_1(n: int) -> None:
    """
    compute the time complexity of running
    this function as a function of n.
    """
    temp_list = list()
    for i in range(n**2):
        temp = 0
        for j in range(i):
            temp += j
        temp_list.append(temp)
    sum(temp_list)
    

def function_2(n: int) -> None:
    """
    compute the time complexity of running
    this function as a function of n.

    do not hesitate to do some reseach about the
    complexity of the functions used and to average
    the measured times over a number of trials if necessary.
    """
    print(n)
    for i in range(n):
        temp_list = [j+i for j in range(n)]
        shuffle(temp_list)
        max(temp_list)




import time
import matplotlib.pyplot as plt
import numpy as np

def measure_function_time(func, n):
    start_time = time.time()
    func(n)
    return time.time() - start_time

# Measure execution times for function_1
n_values = [20, 40, 80, 150, 300]
times_function_1 = [measure_function_time(function_1, n) for n in n_values]

# Fit a polynomial curve to the measured times
coefficients_function_1 = np.polyfit(n_values, times_function_1, deg=4)  # degree 4 for O(n^4)
poly_function_1 = np.poly1d(coefficients_function_1)

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(n_values, times_function_1, label='Measured Times')
plt.plot(n_values, poly_function_1(n_values), label=f'Fitted Polynomial (Degree {len(coefficients_function_1)-1})', color='r')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity Analysis of function_1')
plt.legend()
plt.grid(True)
plt.show()

print(f"Fitted Polynomial Coefficients: {coefficients_function_1}")

# Measure execution times for function_2
times_function_2 = [measure_function_time(function_2, n) for n in n_values]

# Fit a polynomial curve to the measured times
coefficients_function_2 = np.polyfit(n_values, times_function_2, deg=2)  # degree 2 for O(n^2) (since shuffle and max are O(n))
poly_function_2 = np.poly1d(coefficients_function_2)

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(n_values, times_function_2, label='Measured Times')
plt.plot(n_values, poly_function_2(n_values), label=f'Fitted Polynomial (Degree {len(coefficients_function_2)-1})', color='r')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity Analysis of function_2')
plt.legend()
plt.grid(True)
plt.show()

print(f"Fitted Polynomial Coefficients: {coefficients_function_2}")
