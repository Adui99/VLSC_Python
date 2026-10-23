# Bài 1 — Sắp xếp điểm
# Cho mảng điểm [78, 55, 90, 65, 88, 45]. 
# Sắp xếp tăng dần và giảm dần; tìm điểm cao nhất, thấp nhất 
# và vị trí của chúng.

import numpy as np
arr = np.array([78, 55, 90, 65, 88, 45])
print(arr)
# Sắp xếp tăng dần
arr1 = np.sort(arr)
print(arr1)
# Sắp xếp giảm dần
arr2 = np.sort(arr)[::-1]
print(arr2)
# Tìm điểm cao nhất
max_score = np.max(arr)
print(max_score)
# Tìm điểm thấp nhất
min_score = np.min(arr)
print(min_score)
# Tìm vị trí của điểm cao nhất
index_max = np.where(arr == max_score)
print(index_max)
# Tìm vị trí của điểm thấp nhất
index_min = np.where(arr == min_score)
print(index_min)