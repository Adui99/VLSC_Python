# def check_number(n):
#     if (n % 2 == 0):
#         return "Even"
#     return "Odd"

# print(check_number(5))
# print(check_number(10))


# def check_number(n):
#     return "Even" if n % 2 == 0 else "Odd"

# print(check_number(5))
# print(check_number(10))


#ham lamda
is_check = lambda x : "Even" if x % 2 == 0 else "Odd"

print(is_check(5))
print(is_check(10))