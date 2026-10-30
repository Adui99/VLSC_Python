import numpy as np
import pandas as pd 

# Kham pha du lieu
df = pd.read_csv("sales_practice_dataset.csv", encoding = "utf-8")

print(df.head())
print(df.tail(3))
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()
print(df.describe())

# Kiem tra du lieu thieu
print(df.isna().sum())
print("Tong o thieu:", df.isna().sum().sum())

missing_row = df[df.isna().any(axis=1)]
print(missing_row)

# Chuan hoa van ban
df["Product"] = df["Product"].str.strip()
df["City"] = df["City"].str.strip()
df["Category"] = df["Category"].str.strip()

print(df["Product"].unique())
print(df["City"].unique())

# Phat hien gia tri khong hop le
print(df[df["Quantity"] <= 0])
print(df[df["UnitPrice"] <= 0])
print(df[df["Quantity"] > 50])

invalid = df[
    (df["Quantity"] <= 0) |
    (df["UnitPrice"] <= 0)
]
print(invalid)

# Phat hien ngoai lai bang IQR
quantity = df["Quantity"].dropna()

Q1 = quantity.quantile(0.25)
Q3 = quantity.quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Ghi chu loi 1: Ban dau mask = df[...] (DataFrame 2D) truyen vao df.loc[mask, ...]
# bi loi "ValueError: Cannot index with multidimensional key".
# Cach chuan: mask la Series boolean 1D:
mask = (
    (df["Quantity"] < lower) |
    (df["Quantity"] > upper)
)
print("Q1:", Q1, "Q3:", Q3, "IQR:", IQR)
print("Nguong duoi:", lower, "Nguong tren:", upper)
print(df.loc[mask, ["OrderID", "Quantity"]])

# 6. Ap dung quy tac lam sach co can cu va luu DataFrame moi (Theo quytrinh.txt)
# Ghi chu loi 2: Ban dau chua tao bien clean_df gay loi "NameError: name 'clean_df' is not defined".
# Quy tac lam sach:
# - Loai bo dong thieu du lieu (NaN)
# - Loai bo dong khong hop le (Quantity <= 0 hoac UnitPrice <= 0)
# - Loai bo gia tri ngoai lai bat thuong (Quantity > 50 sau khi da dieu tra bang IQR)
clean_df = df.dropna().copy()
clean_df = clean_df[
    (clean_df["Quantity"] > 0) &
    (clean_df["UnitPrice"] > 0) &
    (clean_df["Quantity"] <= 50)
].copy()

# Tinh doanh thu va phan tich
clean_df["Revenue"] = clean_df["Quantity"] * clean_df["UnitPrice"]

print("Tong doanh thu:", clean_df["Revenue"].sum())

by_product = (
    clean_df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
print(by_product)

by_city = (
    clean_df.groupby("City")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
print(by_city)

# Ma hoa du lieu phan loai
encoded_df = pd.get_dummies(
    clean_df,
    columns=["Category", "City"],
    dtype=int
)
print(encoded_df.head())

# Anh xa nhan co thu tu
priority_map = {"Low": 1, "Medium": 2, "High": 3}
# Nếu có cột Priority:
# df["PriorityCode"] = df["Priority"].map(priority_map)

# Xuat CSV va Excel
clean_df.to_csv(
    "sales_clean.csv",
    index=False,
    encoding="utf-8-sig"
)

with pd.ExcelWriter("sales_report.xlsx", engine="openpyxl") as writer:
    clean_df.to_excel(writer, sheet_name="CleanData", index=False)
    by_product.to_frame("Revenue").to_excel(writer, sheet_name="ByProduct")
    by_city.to_frame("Revenue").to_excel(writer, sheet_name="ByCity")


