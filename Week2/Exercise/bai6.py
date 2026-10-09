# User nhap ho ten, tuoi => ghi thong tin vao data2.txt
f6 = open("data2.txt", "a", encoding = "utf-8")
print("Nhap ho ten")
hoten = input()
print("Nhap tuoi")
tuoi = input()
f6.write(str(hoten) + "\n")
f6.write(str(tuoi) + "\n")
f6.write("-------" + "\n")
print("Da ghi thong tin vao file data2.txt")
f6.close()

