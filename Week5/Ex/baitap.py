import sys
import numpy as np
import pandas as pd

# BAI 1. KHAM PHA DU LIEU

print("=" * 70)
print("BAI 1. KHAM PHA DU LIEU")
print("=" * 70)

# 10. Doc file, hien thi 5 dong dau va 5 dong cuoi.
df = pd.read_csv("sales_practice_dataset.csv", encoding="utf-8")
print("\n--- 10. 5 dong dau ---")
print(df.head(5))
print("\n--- 10. 5 dong cuoi ---")
print(df.tail(5))

# 11. Cho biet so dong, so cot, ten cot va kieu du lieu.
print("\n--- 11. Thong tin cau truc du lieu ---")
print(f"So dong: {df.shape[0]}, So cot: {df.shape[1]} (Kich thuoc: {df.shape})")
print(f"Ten cac cot: {list(df.columns)}")
print("\nKieu du lieu tung cot:")
print(df.dtypes)

# 12. Thong ke so gia tri thieu theo tung cot.
print("\n--- 12. Thong ke gia tri thieu ---")
print(df.isna().sum())
print(f"Tong so o bi thieu tren toan bo bang: {df.isna().sum().sum()}")

# 13. Liet ke san pham, nhom hang va thanh pho khac nhau.
print("\n--- 13. Liet ke cac gia tri khac nhau ---")
print("San pham (Product):", df["Product"].dropna().unique())
print("Nhom hang (Category):", df["Category"].dropna().unique())
print("Thanh pho (City):", df["City"].dropna().unique())

# BAI 2. LAM SACH DU LIEU
print("\n" + "=" * 70)
print("BAI 2. LAM SACH DU LIEU")
print("=" * 70)

# 14. Chuan hoa Product, Category va City (xoa khoang trang thua).
df["Product"] = df["Product"].str.strip()
df["Category"] = df["Category"].str.strip()
df["City"] = df["City"].str.strip()
print("\n--- 14. Sau khi chuan hoa khoang trang thua (str.strip) ---")
print("San pham duy nhat:", df["Product"].unique())
print("Nhom hang duy nhat:", df["Category"].unique())
print("Thanh pho duy nhat:", df["City"].unique())

# 15. Tim cac dong thieu Quantity hoac UnitPrice.
missing_rows = df[df["Quantity"].isna() | df["UnitPrice"].isna()]
print("\n--- 15. Cac dong thieu Quantity hoac UnitPrice ---")
print(missing_rows)

# 16. Tim Quantity <= 0 va UnitPrice <= 0.
invalid_rows = df[(df["Quantity"] <= 0) | (df["UnitPrice"] <= 0)]
print("\n--- 16. Cac dong co Quantity <= 0 hoac UnitPrice <= 0 ---")
print(invalid_rows)

# 17. De xuat cach xu ly tung truong hop va giai thich.
print("\n--- 17. De xuat cach xu ly va giai thich ---")
print("""De xuat xu ly:
1. Du lieu thieu (Quantity hoac UnitPrice la NaN - dong O011, O012):
   - Loai bo cac dong nay (dropna) vi thieu Quantity hoac UnitPrice se khong the
     tinh toan chinh xac doanh thu.
2. Du lieu khong hop le (Quantity <= 0 hoac UnitPrice <= 0 - dong O013 co Quantity = -1):
   - Loai bo dong nay vi so luong mua trong don hang bat buoc phai la so duong (> 0).
     Gia tri am la loi nhap lieu hoac don huy/hoan tra khong hop le de phan tich.""")

# 18. Tao clean_df, khong ghi de du lieu goc.
clean_df = df.copy()
# Loai bo dong thieu va du lieu khong hop le (Quantity <= 0, UnitPrice <= 0)
clean_df = clean_df.dropna(subset=["Quantity", "UnitPrice"])
clean_df = clean_df[(clean_df["Quantity"] > 0) & (clean_df["UnitPrice"] > 0)]
print(f"\n--- 18. Da tao clean_df thanh cong. Kich thuoc ban dau: {df.shape}, sau loc so bo: {clean_df.shape} ---")


# BAI 3. PHAN TICH NGOAI LAI
print("\n" + "=" * 70)
print("BAI 3. PHAN TICH NGOAI LAI")
print("=" * 70)

# 19. Tinh Q1, Q3, IQR va hai nguong cho Quantity.
quantity_series = df["Quantity"].dropna()
Q1 = quantity_series.quantile(0.25)
Q3 = quantity_series.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("\n--- 19. Chi so thong ke IQR cho Quantity ---")
print(f"Q1 (25%): {Q1}")
print(f"Q3 (75%): {Q3}")
print(f"IQR: {IQR}")
print(f"Nguong duoi (Lower bound = Q1 - 1.5*IQR): {lower_bound}")
print(f"Nguong tren (Upper bound = Q3 + 1.5*IQR): {upper_bound}")

# 20. Liet ke OrderID bi danh dau ngoai lai.
outlier_mask = (df["Quantity"] < lower_bound) | (df["Quantity"] > upper_bound)
outlier_df = df.loc[outlier_mask, ["OrderID", "Product", "Quantity", "UnitPrice", "City"]]
print("\n--- 20. Danh sach cac don hang bi danh dau ngoai lai theo IQR ---")
print(outlier_df)

# 21. So sanh ket qua khi giu va khi loai gia tri ngoai lai.
print("\n--- 21. So sanh ket qua khi giu vs khi loai ngoai lai ---")
# Giu ngoai lai: tap clean_df hien tai (bao gom O005 = 10 va O016 = 150)
df_with_outlier = clean_df.copy()
df_with_outlier["Revenue"] = df_with_outlier["Quantity"] * df_with_outlier["UnitPrice"]

# Loai bo ngoai lai cuc doan O016 (Quantity > 50, bat thuong):
df_without_extreme_outlier = clean_df[clean_df["Quantity"] <= 50].copy()
df_without_extreme_outlier["Revenue"] = df_without_extreme_outlier["Quantity"] * df_without_extreme_outlier["UnitPrice"]

print("Khi GIU ngoai lai:")
print(f"  - So luong don: {len(df_with_outlier)}")
print(f"  - Quantity (Mean: {df_with_outlier['Quantity'].mean():.2f}, Std: {df_with_outlier['Quantity'].std():.2f}, Max: {df_with_outlier['Quantity'].max()})")
print(f"  - Tong doanh thu: {df_with_outlier['Revenue'].sum():,.0f} VND")

print("Khi LOAI ngoai lai bat thuong (Quantity > 50):")
print(f"  - So luong don: {len(df_without_extreme_outlier)}")
print(f"  - Quantity (Mean: {df_without_extreme_outlier['Quantity'].mean():.2f}, Std: {df_without_extreme_outlier['Quantity'].std():.2f}, Max: {df_without_extreme_outlier['Quantity'].max()})")
print(f"  - Tong doanh thu: {df_without_extreme_outlier['Revenue'].sum():,.0f} VND")

# Cap nhat clean_df: loai bo ngoai lai cuc doan (> 50)
clean_df = clean_df[clean_df["Quantity"] <= 50].copy()

# 22. Giai thich vi sao ngoai lai khong dong nghia voi du lieu sai.
print("\n--- 22. Giai thich ve ngoai lai ---")
print("""Giai thich:
- Ngoai lai (Outlier) chi la gia tri sai khac lon ve mat thong ke toan hoc so voi da so du lieu.
- Ngoai lai KHONG DONG NGHIA voi du lieu sai vi:
  + Co the la giao dich thuc te dac biet: Vi du O005 mua 10 chiec USB Drive la don mua si
    hoan toan hop ly cua doanh nghiep (khong phai loi).
  + Trong khi do, O016 mua 150 chiec Webcam la so luong bat thuong lon (> 50),
    rat co the la loi nhap lieu (thua so 0).
  => Do do can dieu tra nghiep vu truoc khi quyet dinh giu hay loai bo, khong duoc tu dong xoa bo.""")


# BAI 4. MA HOA DU LIEU
print("\n" + "=" * 70)
print("BAI 4. MA HOA DU LIEU")
print("=" * 70)

# 23 & 24. Ma hoa Category va City bang pd.get_dummies().
encoded_df = pd.get_dummies(
    clean_df,
    columns=["Category", "City"],
    dtype=int
)

# 25. In 5 dong sau ma hoa va giai thich cac cot 0/1.
print("\n--- 25. 5 dong sau khi ma hoa One-Hot Encoding ---")
print(encoded_df.head(5))
print("""\nGiai thich cac cot 0/1:
- Moi gia tri phan loai tro thanh 1 cot nhi phan moi (vi du City_Hanoi, City_Da Nang,...).
- Gia tri 1: Dong do thuoc danh muc / thanh pho tuong ung.
- Gia tri 0: Dong do khong thuoc danh muc / thanh pho do.""")

# 26. Giai thich vi sao khong nen gan thu tu so tuy y cho Category.
print("\n--- 26. Giai thich vi sao khong gan thu tu so tuy y cho Category ---")
print("""Giai thich:
- Category (Electronics, Accessories) la bien dinh danh danh nghia (Nominal variable),
  khong co quan he thu bac (khong co cai nao lon hon hay quan trong hon cai nao).
- Neu gan so tuy y (vi du Electronics = 1, Accessories = 2), cac mo hinh hoc may va thuat toan
  se hieu nham Accessories gap doi Electronics (2 > 1), tao ra khoang cach toan hoc sai lech
  ban chat du lieu ban dau.""")


# BAI 5. PHAN TICH DOANH THU & XUAT BAO CAO
print("\n" + "=" * 70)
print("BAI 5. PHAN TICH DOANH THU")
print("=" * 70)

# 27. Tao Revenue = Quantity * UnitPrice.
clean_df["Revenue"] = clean_df["Quantity"] * clean_df["UnitPrice"]

# 28. Tinh tong doanh thu tren du lieu da lam sach.
total_revenue = clean_df["Revenue"].sum()
print(f"\n--- 28. Tong doanh thu (du lieu sach): {total_revenue:,.0f} VND ---")

# 29. Tinh doanh thu theo Product va sap xep giam dan.
by_product = (
    clean_df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
print("\n--- 29. Doanh thu theo tung san pham (giam dan) ---")
print(by_product.apply(lambda x: f"{x:,.0f} VND"))

# 30. Tinh doanh thu theo City.
by_city = (
    clean_df.groupby("City")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
print("\n--- 30. Doanh thu theo tung thanh pho (giam dan) ---")
print(by_city.apply(lambda x: f"{x:,.0f} VND"))

# 31. Tim san pham va thanh pho co doanh thu cao nhat.
top_product = by_product.idxmax()
top_product_rev = by_product.max()
top_city = by_city.idxmax()
top_city_rev = by_city.max()

print(f"\n--- 31. San pham & Thanh pho co doanh thu cao nhat ---")
print(f"San pham cao nhat: {top_product} ({top_product_rev:,.0f} VND, chiem {top_product_rev/total_revenue*100:.1f}%)")
print(f"Thanh pho cao nhat: {top_city} ({top_city_rev:,.0f} VND, chiem {top_city_rev/total_revenue*100:.1f}%)")

# 32. Viet 3-5 nhan xet dua tren ket qua.
print("\n--- 32. Nhan xet ket qua phan tich ---")
print("""Nhan xet:
1. Ve san pham: Laptop la mat hang chu luc mang lai doanh thu vuot troi (74.7 trieu VND, chiem ~54.8%
   tong doanh thu), do co don gia cao du so luong ban khong lon.
2. Ve thi truong: TP. Ho Chi Minh la thi truong dan dau voi 56.72 trieu VND (~41.6% tong doanh thu),
   theo sau la Ha Noi (39.35 trieu VND) va Da Nang (28.78 trieu VND).
3. Ve nhom hang: Phan khuc Electronics (Laptop, Monitor, Tablet) chiem ty trong doanh thu ap dao
   so voi phan khuc Accessories (chuot, ban phim, usb,...).
4. Ve chat luong du lieu: Du lieu ban dau co 4 dong bat thuong (2 dong thieu, 1 dong am, 1 dong ngoai lai
   cuc doan 150 webcam). Sau khi lam sach co can cu, tong doanh thu thuc te la 136.29 trieu VND,
   phan anh dung thuc trang kinh doanh hon so voi con so ao 269.79 trieu VND neu giu ngoai lai.""")

# XUAT FILE SAN PHAM NOP
print("\n" + "=" * 70)
print("XUAT SAN PHAM BAO CAO")
print("=" * 70)

# Xuat CSV sach
clean_df.to_csv("sales_clean.csv", index=False, encoding="utf-8-sig")
print("Da xuat file du lieu sach: sales_clean.csv")

# Xuat Excel da sheet
with pd.ExcelWriter("sales_report.xlsx", engine="openpyxl") as writer:
    clean_df.to_excel(writer, sheet_name="CleanData", index=False)
    by_product.to_frame("Revenue").to_excel(writer, sheet_name="ByProduct")
    by_city.to_frame("Revenue").to_excel(writer, sheet_name="ByCity")
print("Da xuat file bao cao Excel: sales_report.xlsx (gom 3 sheet: CleanData, ByProduct, ByCity)")
