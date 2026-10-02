def count_even(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    return count

print(count_even([10, 15, 22, 31, 40, 55]))