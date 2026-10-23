# Bài 17. Chuẩn hóa dữ liệu
# Cho mảng:
# arr = np.array([20, 40, 60, 80, 100])
# 1. Tính giá trị nhỏ nhất và lớn nhất.
# 2. Chuẩn hóa từng giá trị theo công thức x' = (x - xmin) / (xmax - xmin).
# 3. In mảng sau khi chuẩn hóa.
# 4. Giá trị sau chuẩn hóa nằm trong khoảng từ 0 đến 1.

import numpy as np

arr = np.array([20, 40, 60, 80, 100])
print(arr)
#1. Tính giá trị nhỏ nhất và lớn nhất.
value_min = np.min(arr)
value_max = np.max(arr)
print(value_min, value_max)
#2. Chuẩn hóa từng giá trị theo công thức x' = (x - xmin) / (xmax - xmin).
res = (arr - value_min) / (value_max - value_min)
#3. In mảng sau khi chuẩn hóa.
print(res)
#4. Kiểm tra giá trị có nằm trong khoảng từ 0 đến 1 hay không
is_valid = np.all((res >= 0) & (res <= 1))
print(is_valid)
