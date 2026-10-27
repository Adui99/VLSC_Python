import numpy as np

# Doanh thu các ngày
d1 = np.array([200, 180, 250])
d2 = np.array([0, 220, 270])

# Nối hai mảng
combined = np.concatenate((d1, d2))

# Xóa phần tử tại index 3 (ngày nghỉ, doanh thu = 0)
combined = np.delete(combined, 3)

# Thêm doanh thu Chủ nhật (300) vào cuối mảng
combined = np.append(combined, 300)

print("Mảng doanh thu kết quả:", combined)
print("Tổng doanh thu:", np.sum(combined))
print("Doanh thu lũy kế:", np.cumsum(combined))
print("Mức tăng/giảm giữa 2 ngày liên tiếp:", np.diff(combined))