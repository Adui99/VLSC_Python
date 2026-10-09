# #mo file => thao tac voi file => dong file

# f = open("data.txt", "r", encoding="utf-8")
# content = f.read(5)
# print(content)
# f.close()

# # doc theo con tro
# f = open("baitho.txt", "r", encoding = "utf-8")
# content = f.readline()
# print(content)
# content = f.readline()
# print(content)
# f.close()

# # input : string => output : string
# f = open("numbers.txt", "r", encoding = "utf-8")
# content = f.readline()
# print(content)
# print(type(content))
# f.close()

# # GHI DU LIEU RA FILE
# f = open("output.txt", "w", encoding = "utf-8")
# f.write("Way Station")
# f.close()

# f = open("output2.txt", "a", encoding = "utf-8")
# f.write("Mua he ve con ve keu\n")
# f.close()

f = open("output2.txt", "a", encoding = "utf-8")
f.write("Mua he di ve het keu\n")
f.close()