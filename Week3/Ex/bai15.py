# Bài 15. Nối và so sánh hai mảng
# Cho hai mảng:
# arr1 = np.array([10, 20, 30, 40])
# arr2 = np.array([30, 40, 50, 60])
# 1. Nối hai mảng thành một mảng mới.
# 2. Tìm các giá trị xuất hiện trong cả hai mảng.
# 3. Tạo mảng chứa tất cả giá trị không trùng lặp của hai mảng.
# 4. Sắp xếp kết quả tăng dần.
# 5. Gợi ý: np.concatenate(), np.intersect1d(), np.union1d().

import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([30, 40, 50, 60])
# 1. Nối hai mảng thành một mảng mới.
arr3 = np.concatenate((arr1, arr2))
print(arr3)
# 2. Tìm các giá trị xuất hiện trong cả hai mảng.
arr4 = np.intersect1d(arr1, arr2)
print(arr4)
# 3. Tạo mảng chứa tất cả giá trị không trùng lặp của hai mảng.
arr5 = np.union1d(arr1, arr2)
print(arr5)
# 4. Sắp xếp kết quả tăng dần.
arr6 = np.sort(arr5)
print(arr6)