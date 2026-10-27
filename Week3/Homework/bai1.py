import numpy as np

# Mảng nhiệt độ 7 ngày
temp = np.array([31, 27, 34, 29, 26, 33, 30])

print("Mảng ban đầu:", temp)
print("Sắp xếp tăng dần:", np.sort(temp))
print("Sắp xếp giảm dần:", np.sort(temp)[::-1])

max_val = np.max(temp)
min_val = np.min(temp)
max_idx = np.argmax(temp)
min_idx = np.argmin(temp)

print(f"Nhiệt độ cao nhất: {max_val} tại vị trí index {max_idx} trong mảng ban đầu.")
print(f"Nhiệt độ thấp nhất: {min_val} tại vị trí index {min_idx} trong mảng ban đầu.")