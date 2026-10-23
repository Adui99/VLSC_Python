# Bài 13. Tìm các giá trị duy nhất
# Cho mảng mã sản phẩm:
# products = np.array([101, 102, 101, 103, 102, 104, 101, 103])
# 1. Liệt kê các mã sản phẩm không trùng lặp.
# 2. Đếm số lần xuất hiện của từng mã.
# 3. Tìm mã xuất hiện nhiều lần nhất.
# 4. Gợi ý: np.unique(..., return_counts=True).

import numpy as np

products = np.array([101, 102, 101, 103, 102, 104, 101, 103])
# 1. Liệt kê các mã sản phẩm không trùng lặp.
unique_products = np.unique(products)
print(unique_products)
# 2. Đếm số lần xuất hiện của từng mã.
unique_products, counts = np.unique(products, return_counts=True)
print(counts)
# 3. Tìm mã xuất hiện nhiều lần nhất.
max_count = np.max(counts)
max_product = unique_products[np.argmax(counts)]
print(max_product)
