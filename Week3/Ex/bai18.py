# Bài 18. Xử lý dữ liệu ngoài phạm vi
# Cho mảng:
# scores = np.array([-10, 25, 60, 85, 105, 70])
# 1. Giới hạn điểm trong khoảng 0–100.
# 2. In mảng sau khi xử lý.
# 3. Đếm số giá trị ban đầu nhỏ hơn 0.
# 4. Đếm số giá trị ban đầu lớn hơn 100.
# 5. Gợi ý: np.clip(), Boolean indexing.

import numpy as np

scores = np.array([-10, 25, 60, 85, 105, 70])
print(scores)
#1. Giới hạn điểm trong khoảng 0–100.
res = np.clip(scores, 0, 100)
print(res)
#3. Đếm số giá trị ban đầu nhỏ hơn 0.
res1 = scores[scores < 0]
print(res1)
#4. Đếm số giá trị ban đầu lớn hơn 100.
res2 = scores[scores > 100]
print(res2)
