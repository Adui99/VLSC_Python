f = open("data1.txt", "r", encoding = "utf-8")
data = f.read()
data_split = data.split("\n")
# print(data_split)
# print(type(data_split))

sum = 0
for i in range(len(data_split)-1):
    sum += int(data_split[i])
print(sum)
f.close()

f5 = open("data1.txt", "a", encoding = "utf-8")
f5.write(str(sum) + "\n")
f5.close()