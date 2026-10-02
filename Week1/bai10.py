def analyze_numbers(numbers):
    #The largest number
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    #The smallest number
    min = numbers[0]
    for i in numbers:
        if i < min:
            min = i
    #The sum of all numbers
    total = 0
    for i in numbers:
        total += i
    #The average of all numbers
    average = total / len(numbers)
    #The number of even numbers
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1

    return max, min, total, average, count      

print(analyze_numbers([1, 2, 3 ,4 ,5 ,6 ,7 ,8, 9, 10]))    