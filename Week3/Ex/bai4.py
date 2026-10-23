# Bài 4 — Nối và cập nhật
# Tạo hai mảng [1, 2, 3] và [4, 5, 6]. 
# Nối hai mảng, thêm số 7 vào mảng kết quả và 
# xóa phần tử tại index 2.

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1)
print(arr2)
# nối hai mảng
arr3 = np.concatenate((arr1, arr2))
print(arr3)
# thêm số 7 vào mảng kết quả
arr4 = np.append(arr3, 7)
print(arr4)
# xóa phần tử tại index 2
arr5 = np.delete(arr4, 2)
print(arr5)