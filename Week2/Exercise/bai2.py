# viet chuong trinh tim max va min co trong file numbers.txt

# doc file => split => tim max min => print
f = open("numbers.txt", "r", encoding = "utf-8")
content = f.read()
content_split = content.split(" ")
print(content_split)
print(type(content_split))
max = min = int(content_split[0])
for i in range(len(content_split)):
    if int(content_split[i]) > max:
        max = int(content_split[i])
    elif int(content_split[i]) < min:
        min = int(content_split[i])
print("max = ", max)
print("min = ", min)
f.close()

# ghi du lieu ra file output.txt
f2 = open("output.txt", "w", encoding = "utf-8")
f2.write("max = " + str(max) + "\n")
f2.write("min = " + str(min))
f2.close()