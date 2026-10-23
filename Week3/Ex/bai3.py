# Bài 3 — Thống kê phần tử
# Cho mảng [10, 20, 10, 30, 20, 10, 40]. 
# Tìm các giá trị duy nhất và số lần xuất hiện 
# của từng giá trị.

import numpy as np
arr = np.array([10, 20, 10, 30, 20, 10, 40])
print(arr)
# unique values
arr1 = np.unique(arr)
# dem so lan xuat hien
arr2, count = np.unique(arr, return_counts=True)
print(arr2)
print(count)