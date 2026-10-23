# Bài 14. Tìm giá trị gần nhất
# Cho mảng:
# arr = np.array([12, 25, 37, 48, 59, 72, 85])
# 1. Tìm phần tử gần với số 50 nhất.
# 2. Tìm phần tử gần với số 70 nhất.
# 3. In ra giá trị và vị trí tương ứng.
# 4. Gợi ý: np.abs() và np.argmin().

import numpy as np

arr = np.array([12, 25, 37, 48, 59, 72, 85])
# 1. Tìm phần tử gần với số 50 nhất.
res1 = arr[np.abs(arr - 50).argmin()]
print(res1)
# 2. Tìm phần tử gần với số 70 nhất.
res2 = arr[np.abs(arr - 70).argmin()]
print(res2)
# 3. In ra giá trị và vị trí tương ứng.
print(np.argmin(np.abs(arr - 50)))
print(np.argmin(np.abs(arr - 70)))