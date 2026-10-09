def analyze(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average

dataset = [8, 15, 3, 27, 42, 11]
min_val, max_val, avg_val = analyze(dataset)

print("Минимальное:", min_val)
print("Максимальное:", max_val)
print("Среднее:", avg_val)