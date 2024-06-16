import time
import numpy as np
import matplotlib.pyplot as plt

from random import shuffle

def function_1(n: int) -> None:
    temp_list = list()
    for i in range(n**2):
        temp = 0
        for j in range(i):
            temp += j
        temp_list.append(temp)
    sum(temp_list)

def function_2(n: int) -> None:
    print(n)
    for i in range(n):
        temp_list = [j+i for j in range(n)]
        shuffle(temp_list)
        max(temp_list)

# Measure the computation time for a range of n values for both functions
n_values = np.arange(10, 100, 10)
times_function_1 = []
times_function_2 = []

for n in n_values:
    start_time = time.time()
    function_1(n)
    times_function_1.append(time.time() - start_time)

    start_time = time.time()
    function_2(n)
    times_function_2.append(time.time() - start_time)

# Fit polynomials to the measured times
degree_1 = 4  # As derived, function_1 is O(n^4)
degree_2 = 2  # As derived, function_2 is O(n^2)

coeffs_1 = np.polyfit(n_values, times_function_1, degree_1)
poly_1 = np.poly1d(coeffs_1)

coeffs_2 = np.polyfit(n_values, times_function_2, degree_2)
poly_2 = np.poly1d(coeffs_2)

# Plot the measured times and the fitted polynomials
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(n_values, times_function_1, 'o', label='Measured times')
plt.plot(n_values, poly_1(n_values), '-', label=f'Fitted polynomial of degree {degree_1}')
plt.title('Function 1: Time Complexity Analysis')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(n_values, times_function_2, 'o', label='Measured times')
plt.plot(n_values, poly_2(n_values), '-', label=f'Fitted polynomial of degree {degree_2}')
plt.title('Function 2: Time Complexity Analysis')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend()

plt.tight_layout()
plt.show()
