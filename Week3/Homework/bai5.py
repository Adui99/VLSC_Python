import numpy as np

# Mảng điểm ban đầu
scores = np.array([8.34, 10.5, -1, 6.48, 4.96, 7, 3.21])

# Giới hạn điểm trong khoảng 0 - 10
clipped_scores = np.clip(scores, 0, 10)

# Làm tròn đến 1 chữ số thập phân
rounded_scores = np.round(clipped_scores, 1)
print("Điểm sau khi xử lý:", rounded_scores)

# Xếp loại
print("Kết quả xếp loại:")
for score in rounded_scores:
    if score >= 8.0:
        grade = "Giỏi"
    elif score >= 6.5:
        grade = "Khá"
    elif score >= 5.0:
        grade = "Trung bình"
    else:
        grade = "Yếu"
    print(f"- Điểm {score}: {grade}")