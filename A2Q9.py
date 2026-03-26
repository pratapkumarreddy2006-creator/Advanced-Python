import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result_dot = np.dot(a, b)
result_at = a @ b
print(result_dot)
print(result_at)