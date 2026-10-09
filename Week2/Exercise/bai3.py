f3 = open("data1.txt", "w", encoding = "utf-8")
for i in range (1,11):
    f3.write(str(i) + "\n")
f3.close()