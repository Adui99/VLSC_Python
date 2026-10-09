f = open("numbers.txt", "r", encoding = "utf-8")
content = f.read()
print(content)
print(type(content))
content_split = content.split(" ")
print(content_split)
print(type(content_split))
sum = 0
for i in range(len(content_split)):
    sum += int(content_split[i])
print(sum)
f.close()