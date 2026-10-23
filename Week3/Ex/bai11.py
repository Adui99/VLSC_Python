# Bài 11. Lọc số chẵn và số lẻ
# Cho mảng:
# arr = np.array([12, 7, 24, 31, 46, 53, 60, 75])
# 1. Tạo mảng chỉ chứa số chẵn.
# 2. Tạo mảng chỉ chứa số lẻ.
# 3. Đếm số lượng số chẵn và số lượng số lẻ.

import numpy as np

arr = np.array([12, 7, 24, 31, 46, 53, 60, 75])
print(arr)
# 1. Tạo mảng chỉ chứa số chẵn.
odd = arr[arr % 2 == 0]
print(odd)
# 2. Tạo mảng chỉ chứa số lẻ.
even = arr[arr % 2 != 0]
print(even)
# 3. Đếm số lượng số chẵn và số lượng số lẻ.
count_even = np.count_nonzero(arr % 2 == 0)
count_odd = np.count_nonzero(arr % 2 != 0)
print("count even:", count_even)
print("count odd:", count_odd)
