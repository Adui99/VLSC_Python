import numpy as np

# Khởi tạo mảng dữ liệu doanh số 10 ngày
sales = np.array([25, 32, 18, 40, 35, 50, 28, 45, 60, 42])

print("Mảng doanh số ban đầu:", sales)
print("-" * 50)

# 1. Tính tổng số sản phẩm đã bán
total_sales = np.sum(sales)
print(f"1. Tổng số sản phẩm đã bán: {total_sales}")

# 2. Tính số sản phẩm bán trung bình mỗi ngày
mean_sales = np.mean(sales)
print(f"2. Số sản phẩm bán trung bình mỗi ngày: {mean_sales}")

# 3. Tìm ngày bán được nhiều sản phẩm nhất (chỉ số index + 1)
max_day = np.argmax(sales) + 1
print(f"3. Ngày bán được nhiều sản phẩm nhất: Ngày {max_day} ({sales[max_day - 1]} sản phẩm)")

# 4. Tìm ngày bán được ít sản phẩm nhất
min_day = np.argmin(sales) + 1
print(f"4. Ngày bán được ít sản phẩm nhất: Ngày {min_day} ({sales[min_day - 1]} sản phẩm)")

# 5. Liệt kê các ngày bán được trên 40 sản phẩm
days_over_40 = np.where(sales > 40)[0] + 1
print(f"5. Các ngày bán được trên 40 sản phẩm: Ngày {list(days_over_40)} (với số lượng tương ứng: {sales[sales > 40]})")

# 6. Tính doanh số lũy kế theo ngày
cumulative_sales = np.cumsum(sales)
print(f"6. Doanh số lũy kế theo ngày: {cumulative_sales}")

# 7. Tính mức thay đổi số lượng bán được giữa hai ngày liên tiếp
sales_diff = np.diff(sales)
print(f"7. Mức thay đổi giữa hai ngày liên tiếp: {sales_diff}")

# 8. Sắp xếp số lượng bán được theo thứ tự tăng dần
sorted_sales = np.sort(sales)
print(f"8. Số lượng bán theo thứ tự tăng dần: {sorted_sales}")

# 9. Đếm số ngày bán được ít nhất 30 sản phẩm (>= 30)
count_at_least_30 = np.sum(sales >= 30)
print(f"9. Số ngày bán được ít nhất 30 sản phẩm: {count_at_least_30}")

# 10. Thay các giá trị nhỏ hơn 30 thành 30 và in kết quả
modified_sales = np.where(sales < 30, 30, sales)
print(f"10. Mảng sau khi thay các giá trị < 30 thành 30: {modified_sales}")