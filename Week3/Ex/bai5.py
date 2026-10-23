# Bài 5 — Phân tích doanh thu
# Doanh thu trong 5 ngày là [100, 150, 120, 200, 180]. 
# Tính tổng doanh thu, doanh thu lũy kế, và mức tăng 
# hoặc giảm giữa hai ngày liên tiếp.

import numpy as np
doanhthu = np.array([100, 150, 120, 200, 180])
print(doanhthu)
# Tính tổng doanh thu
tong = np.sum(doanhthu)
print("tong doanh thu:", tong)
# Tính doanh thu lũy kế
luyke = np.cumsum(doanhthu)
print("doanh thu luy ke:", luyke)
# Tính mức tăng hoặc giảm giữa hai ngày liên tiếp
muc = np.diff(doanhthu)
print("muc tang giam:", muc)