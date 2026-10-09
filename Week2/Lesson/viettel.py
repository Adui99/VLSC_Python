# buoc 1: mo file
f = open("viettel_data.txt", "r", encoding = "utf-8")
# buoc 2: doc file
data = f.read()
data = data.split(",")
# print(data)
# print(type(data))
# buoc 3: xu ly 
get_data = data[len(data) - 1]
total = int(get_data) * 1000
# buoc 4: xuat ket qua
print(total)
f.close()