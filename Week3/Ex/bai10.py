# Bài 10. Kiểm tra điều kiện
# Cho mảng:
# arr = np.array([12, 18, 25, 30, 42, 55])
# 1. Kiểm tra tất cả phần tử có lớn hơn 10 hay không.
# 2. Kiểm tra có phần tử nào lớn hơn 50 hay không.
# 3. Kiểm tra tất cả phần tử có nằm trong khoảng từ 10 đến 60 hay không.
# 4. Gợi ý: np.all(), np.any().

import numpy as np

arr = np.array([12, 18, 25, 30, 42, 55])
print(arr)

# 1. Kiểm tra tất cả phần tử có lớn hơn 10 hay không.
check_1 = np.all(arr > 10)
print(check_1)

# 2. Kiểm tra có phần tử nào lớn hơn 50 hay không.
check_2 = np.any(arr > 50)
print(check_2)

# 3. Kiểm tra tất cả phần tử có nằm trong khoảng từ 10 đến 60 hay không.
check_3 = np.all((arr >= 10) & (arr <= 60))
print(check_3)
