import pandas as pd
import numpy as np

# 1. Đọc file CSV
df = pd.read_csv("pandas_sales_practice.csv", encoding="utf-8")

# 2. Hiển thị 5 dòng đầu, 5 dòng cuối, số dòng, số cột và kiểu dữ liệu
print("--- 5 dòng đầu ---")
print(df.head())

print("\n--- 5 dòng cuối ---")
print(df.tail())

print(f"\nKích thước dữ liệu (Số dòng, Số cột): {df.shape}")
print("\nTên các cột:")
print(df.columns)

print("\n--- Thông tin tổng quát ---")
print(df.info())

print("\n--- Kiểu dữ liệu ---")
print(df.dtypes)

print("\n--- Thống kê mô tả ---")
print(df.describe())

print("\n-----------------------")
# 3. Kiểm tra dữ liệu thiếu trong từng cột
print("\n--- Dữ liệu thiếu trong từng cột ---")
print(df.isna().sum())
print("\n-----------------------")

# Lọc các dòng bị thiếu dữ liệu
missing_row = df[df.isna().any(axis=1)]
print("\n--- Các dòng bị thiếu dữ liệu ---")
print(missing_row)
print("\n-----------------------")

# 4. Chuẩn hóa tên sản phẩm và thành phố bằng str.strip()
df["Product"] = df["Product"].str.strip()
df["City"] = df["City"].str.strip()
print(df)
print("\n-----------------------")

# 5. Phát hiện số lượng bán không hợp lệ (số âm hoặc quá lớn bất thường > 50)
invalid_quantity = df[(df["Quantity"] < 0) | (df["Quantity"] > 50)]
print("\n--- Số lượng không hợp lệ ---")
print(invalid_quantity)
print("\n-----------------------")

# Làm sạch dữ liệu sai bằng cách gán về NaN để xử lý đồng bộ
df.loc[(df["Quantity"] < 0) | (df["Quantity"] > 50), "Quantity"] = np.nan
print("\n-----------------------")

# 6. Xử lý dữ liệu thiếu và không hợp lệ trong Quantity và UnitPrice
# Thay thế giá trị NaN bằng giá trị trung vị (median) của từng sản phẩm tương ứng
df["Quantity"] = df["Quantity"].fillna(df.groupby("Product")["Quantity"].transform("median"))
df["UnitPrice"] = df["UnitPrice"].fillna(df.groupby("Product")["UnitPrice"].transform("median"))

# Kiểm tra lại dữ liệu thiếu sau khi xử lý
print("\n--- Dữ liệu thiếu sau khi xử lý ---")
print(df.isna().sum())
print("\n-----------------------")

# 7. Tạo cột Revenue = Quantity * UnitPrice
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
print("\n-----------------------")

# 8. Tính tổng doanh thu theo từng sản phẩm
rev_by_product = df.groupby("Product")["Revenue"].sum()
print("\n--- Tổng doanh thu theo từng sản phẩm ---")
print(rev_by_product)
print("\n-----------------------")

# 9. Thống kê doanh thu theo từng thành phố
rev_by_city = df.groupby("City")["Revenue"].sum()
print("\n--- Thống kê doanh thu theo từng thành phố ---")
print(rev_by_city)
print("\n-----------------------")

# 10. Sắp xếp sản phẩm theo doanh thu giảm dần
sorted_products = rev_by_product.sort_values(ascending=False)
print("\n--- Sản phẩm theo doanh thu giảm dần ---")
print(sorted_products)
print("\n-----------------------")

# 11. Xuất dữ liệu đã xử lý ra file sales_clean.csv
df.to_csv("sales_clean.csv", index=False, encoding="utf-8")
print("\nĐã xuất file dữ liệu đã xử lý thành công ra: sales_clean.csv")
print("\n-----------------------")
