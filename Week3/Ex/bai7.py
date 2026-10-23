# Bài 7. Đảo ngược mảng
# Cho mảng:
# arr = np.array([12, 25, 38, 41, 56, 69])
# 1. In mảng theo thứ tự ngược lại.
# 2. In 3 phần tử cuối theo thứ tự ban đầu.
# 3. In các phần tử ở vị trí chẵn (index chẵn).

import numpy as np

arr = np.array([12, 25, 38, 41, 56, 69])
print(arr)
# 1. In mảng theo thứ tự ngược lại.
arr1 = arr[::-1]
print(arr1)
# 2. In 3 phần tử cuối theo thứ tự ban đầu.
arr2 = arr[-3:]
print(arr2)
# 3. In các phần tử ở vị trí chẵn (index chẵn).
arr3 = arr[::2]
print(arr3)