# Bài 16. Tính tổng tích lũy và độ thay đổi
# Doanh thu trong 7 ngày:
# revenue = np.array([100, 120, 90, 150, 180, 160, 200])
# 1. Tính tổng doanh thu.
# 2. Tính doanh thu lũy kế theo từng ngày.
# 3. Tính mức tăng hoặc giảm so với ngày trước.
# 4. Tìm ngày có doanh thu cao nhất.
# 5. Gợi ý: np.cumsum(), np.diff(), np.argmax().

import numpy as np

revenue = np.array([100, 120, 90, 150, 180, 160, 200])
#1. tính tổng doanh thu
res1 = np.sum(revenue)
print(res1)
#2. Tính doanh thu lũy kế theo từng ngày.
res2 = np.cumsum(revenue)
print(res2)
#3. Tính mức tăng hoặc giảm so với ngày trước.
res3 = np.diff(revenue)
print(res3)
#4. Tìm ngày có doanh thu cao nhất.
res4 = np.argmax(revenue)
print(res4)