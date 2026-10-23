# Bài 2 — Lọc và đếm
# Cho mảng [35, 60, 75, 45, 90, 80, 50]. 
# In ra các số từ 50 đến dưới 80, sau đó đếm số phần tử 
# thỏa mãn điều kiện.

import numpy as np
arr = np.array([35, 60, 75, 45, 90, 80, 50])
print(arr)
# Lọc các số từ 50 đến dưới 80
arr1 = np.where((arr >= 50) & (arr < 80))
print(arr1)
# Đếm số phần tử thỏa mãn điều kiện
count = np.count_nonzero((arr >= 50) & (arr < 80))
print(count)
