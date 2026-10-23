# Bài 8. Thay thế các phần tử
# Cho mảng:
# arr = np.array([10, 25, 30, 45, 50, 65, 70])
# 1. Thay các phần tử nhỏ hơn 30 bằng 0.
# 2. Thay các phần tử lớn hơn 60 bằng 100.
# 3. In mảng sau khi cập nhật.

import numpy as np

arr = np.array([10, 25, 30, 45, 50, 65, 70])
print(arr)
# 1. Thay các phần tử nhỏ hơn 30 bằng 0.
arr1 = np.where(arr < 30, 0, arr)
print(arr1)
# 2. Thay các phần tử lớn hơn 60 bằng 100.
arr2 = np.where(arr > 60, 100, arr)
print(arr2)