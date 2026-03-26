import numpy as np
arr = np.array([50, 20, 40, 10, 30])
asc = np.sort(arr)
desc = np.sort(arr)[::-1]
print("Original Array:", arr)
print("Ascending Order:", asc)
print("Descending Order:", desc)