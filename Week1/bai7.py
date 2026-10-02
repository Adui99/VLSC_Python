def calculate_average(scores):
    total = 0
    for i in scores:
        total += i
    average = total / len(scores)
    return average

print(calculate_average([8, 7, 9, 6 ,10]))