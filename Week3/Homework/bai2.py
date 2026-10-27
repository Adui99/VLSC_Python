import numpy as np

# Mảng ban đầu
arr = np.array([42, 67, 85, 51, 73, 98, 60, 39, 80])

# Lọc các số lớn hơn 50 và không vượt quá 80
filtered_arr = arr[(arr > 50) & (arr <= 80)]

print("Các số lớn hơn 50 và không vượt quá 80:", filtered_arr)
print("Số lượng phần tử thỏa điều kiện:", len(filtered_arr))
print("Giá trị trung bình:", np.mean(filtered_arr))