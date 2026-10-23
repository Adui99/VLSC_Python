# Bài 6 — Xử lý điểm
# Cho mảng [45, 120, -5, 75, 95, 60]. 
# Giới hạn điểm trong khoảng 0–100, làm tròn đến số nguyên
# nếu cần, rồi phân loại điểm từ 50 trở lên là Đạt, 
# còn lại là Không đạt.

import numpy as np
diem = np.array([45, 120, -5, 75, 95, 60])
print(diem)
# Giới hạn điểm trong khoảng 0-100
diem1 = np.clip(diem, 0, 100)
print(diem1)
# làm tròn đến số nguyên
diem1 = np.round(diem1)
print(diem1)
# phân loại điểm từ 50 trở lên là Đạt, còn lại là Không đạt.
diem2 = np.where(diem1 >= 50, "Đạt", "Không đạt")
print(diem2)