# Bài 12. Phân tích điểm thi
# Cho mảng điểm:
# scores = np.array([45, 78, 90, 55, 62, 88, 35, 95, 70, 48])
# 1. Tính điểm trung bình.
# 2. Đếm số sinh viên đạt điểm từ 50 trở lên.
# 3. Lọc các điểm từ 80 trở lên.
# 4. Tìm điểm cao nhất và thấp nhất.
# 5. Tính tỷ lệ phần trăm sinh viên đạt điểm từ 50 trở lên.

import numpy as np

scores = np.array([45, 78, 90, 55, 62, 88, 35, 95, 70, 48])
# 1. Tinh diem trung binh
dtb = scores.mean()
print(dtb)
# 2. Đếm số sinh viên đạt điểm từ 50 trở lên.
count = np.sum(scores >= 50)
print(count)
# 3. Lọc các điểm từ 80 trở lên.
scores1 = scores[scores >= 80]
print(scores1)
# 4. Tìm điểm cao nhất và thấp nhất.
diem_cao_nhat = np.max(scores)
diem_thap_nhat = np.min(scores)
print(diem_cao_nhat)
print(diem_thap_nhat)

