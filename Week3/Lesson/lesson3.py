import numpy as np
# print(np.__version__)
# # Tao 1 mang voi cac pt la so 0
# arr = np.zeros(5)
# print(arr)

# # Tao 1 mang voi cac pt la so 2
# arr = np.full(5, 2)
# print(arr)

# # Tao 1 mang voi cac pt la so 3
# arr = np.full(5, 3)
# print(arr)

# # Tao 1 mang voi cac pt la so 4
# arr = np.ones(5) * 4
# print(arr)

# # Tao 1 mang voi arange - tao 1 day so
# arr = np.arange(1, 10) #start => stop - 1 / (step)
# print(arr)

# # Tao 1 mang voi arange - tao 1 day so
# arr = np.arange(5, 20, 5) #start => stop - 1 / (step)
# print(arr)

# # Tao 1 mang voi arange - tao 1 day so cach deu nhau
# arr = np.arange(0, 10, 5) #start => stop - 1 / (step)
# print(arr)

# # Tao 1 mang voi arange - tao 1 day so random
# arr = np.random.randint(1, 101, size = 5) # 1 - 100 random voi 5 pt
# print(arr)

# # Thao tac voi mang 1 chieu thu vien numpy
# arr = np.array([10, 20, 30, 40, 50])
# print(arr[0]) # truy cap phan tu dau tien 
# print(arr[1:4]) # truy cap phan tu tu vi tri thu 2 den 4
# print(arr[:3]) # truy cap phan tu tu vi tri thu 1 den 3
# print(arr[3:]) # truy cap phan tu tu vi tri thu 4 den het
# print(arr[::2]) # truy cap cac pt cach 2 don vi 
# arr[1:4] = 0 # thay doi gia tri cac phan tu trong mang 
# print(arr) # 10 0 0 0 50

# # arimethic operations
# arr = np.array([10, 20, 30, 40])
# print(arr + 5) # 15 25 35 45
# print(arr - 5) # 5 15 25 35
# print(arr * 2) # 20 40 60 80
# print(arr / 10) # 1 2 3 4
# print(arr ** 2) # 100 400 900 1600

# # useful properties - functions
# arr = np.array([10, 20, 30, 40])
# print(arr.ndim) # dimensions
# print(arr.shape) # shape
# print(arr.size) # size
# print(arr.dtype) # data type

# print(np.sum(arr)) # tong cac phan tu
# print(np.min(arr)) # gia tri nho nhat
# print(np.max(arr)) # gia tri lon nhat
# print(np.mean(arr)) # gia tri trung binh
# print(np.std(arr)) # do lech chuan

# # filtering e using condition : loc theo dieu kien
# scores = np.array([45, 60, 75, 85, 95])
# print(scores >= 70) # dieu kien
# print(scores[scores >= 70]) # loc va in ket qua
# # sap xep mang tang dan
# scores = np.array([45, 75, 60, 85, 95])
# print(np.sort(scores))
# # sap xep mang giam dan
# print(np.sort(scores)[::-1])
# print(scores[(scores >= 60) & (scores < 90)])

# scores[scores < 50] = 50
# print(scores) # 50 60 75 85 95

# # tim theo dk - where
# position = np.where(scores >= 80)
# print(position)
# # phan loai diem dat va chua dat
# result = np.where(scores >= 80, "pass", "failed")
# print(result)
# # dem pt thoa dk
# print(np.sum(scores >= 70))
# print(np.count_nonzero(scores >= 70))
# lay cac pt duy nhat unique()
# arr = np.array([10, 20, 10, 30, 20, 40, 30])
# print(np.unique(arr))
# # dem so lan xuat hien cua pt
# values, counts = np.unique(arr, return_counts=True)
# print(values)
# print(counts)

# arr1 = np.array([10, 20, 30])
# arr2 = np.array([40, 50, 60])
# result = np.concatenate((arr1, arr2))
# print(result) 

# # them 1 pt
# arr = np.array([10, 20, 30])
# result = np.append(arr, 50)
# print(result)

# # xoa 1 pt
# arr = np.array([10, 20, 30, 40, 50])
# result = np.delete(arr, 2)
# print(result)

# # xoa nhieu vi tri
# arr = np.array([10, 20, 30, 40, 50])
# result = np.delete(arr, [1, 3])
# print(result)   

# gioi han gia tri clip()
# Dua cac gia tri nho hon nguon toi thieu len cai nguong do 
# va cac gia tri lon hon nguong toi da len cai nguong do 
scores = np.array([-10, 30, 60, 90, 120])
result = np.clip(scores, 0, 100)
print(result) 

# chuyen doi kieu du lieu
result = scores.astype(float)
print(result)
print(result.dtype)
# ham lam tron so
arr = np.array([2.345, 3.678, 4.567])
print(np.round(arr, 2)) # lam tron so 2 con sau dau phay
print(np.round(arr)) # lam tron so 
 