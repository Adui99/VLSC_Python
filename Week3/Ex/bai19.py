# Bài 19. Quản lý điểm sinh viên
# Một lớp có điểm thi của 15 sinh viên:
# scores = np.array([
# 45, 67, 80, 92, 55,
# 73, 88, 39, 95, 61,
# 70, 84, 50, 77, 90
# ])
# 1. In danh sách điểm ban đầu.
# 2. Tính điểm trung bình của lớp.
# 3. Tìm điểm cao nhất, thấp nhất và vị trí tương ứng.
# 4. Đếm số sinh viên đạt và không đạt, với điểm đạt từ 50 trở lên.
# 5. Lọc danh sách sinh viên có điểm từ 80 trở lên.
# 6. Sắp xếp điểm theo thứ tự giảm dần.
# 7. Tính tỷ lệ sinh viên đạt yêu cầu theo phần trăm.
# 8. Thay các điểm dưới 40 thành 40 và in danh sách sau cập nhật.

import numpy as np

scores = np.array([45, 67, 80, 92, 55, 73, 88, 39, 95, 61, 70, 84, 50, 77, 90])
print(scores)
# 2. Tính điểm trung bình của lớp.
print(scores.mean())
# 3. Tìm điểm cao nhất, thấp nhất và vị trí tương ứng.
value_min = np.min(scores)
print(value_min)
value_max = np.max(scores)
print(value_max)
position_min = np.where(scores == value_min)[0]
print(position_min)
position_max = np.where(scores == value_max)[0]
print(position_max)
# 4. Đếm số sinh viên đạt và không đạt, với điểm đạt từ 50 trở lên.
count_pass = np.count_nonzero(scores >= 50)
print(count_pass)
count_not_pass = np.count_nonzero(scores < 50)
print(count_not_pass)
# 5. Lọc danh sách sinh viên có điểm từ 80 trở lên.
arr1 = scores[scores >= 80]
print(arr1)
# 6. Sắp xếp điểm theo thứ tự giảm dần.
arr2 = np.sort(scores)[::-1]
print(arr2)
# 7. Tính tỷ lệ sinh viên đạt yêu cầu theo phần trăm.
ty_le = (count_pass / len(scores)) * 100
print(ty_le)
# 8. Thay các điểm dưới 40 thành 40 và in danh sách sau cập nhật.
res = np.where(scores < 40, 40, scores)
print(res)