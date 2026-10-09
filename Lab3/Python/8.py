def calculate_sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

def find_min(numbers):
    minimum = numbers[0]
    for x in numbers[1:]:
        if x < minimum:
            minimum = x
    return minimum

def find_max(numbers):
    maximum = numbers[0]
    for x in numbers[1:]:
        if x > maximum:
            maximum = x
    return maximum

nums = [17, 3, 49, -8, 22, 65, 0]
print("Сумма (своя / встроенная):", calculate_sum(nums), sum(nums))
print("Минимум (свой / встроенный):", find_min(nums), min(nums))
print("Максимум (свой / встроенный):", find_max(nums), max(nums))