import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr[2])   
print(arr[:3])   
print(arr[2:])    
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
print(arr2d[0, :])
print(arr2d[:, 1])
print(arr2d[0:2, 1:3])