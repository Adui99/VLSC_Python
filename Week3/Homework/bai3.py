import numpy as np

# Mảng ban đầu
arr = np.array([3, 7, 3, 9, 7, 3, 5, 9, 3])

# Tìm các giá trị duy nhất và số lần xuất hiện
unique_vals, counts = np.unique(arr, return_counts=True)

print("Các giá trị duy nhất:", unique_vals)
for val, count in zip(unique_vals, counts):
    print(f"- Giá trị {val}: xuất hiện {count} lần")

# Giá trị xuất hiện nhiều nhất
most_frequent = unique_vals[np.argmax(counts)]
print(f"Giá trị xuất hiện nhiều nhất: {most_frequent}")