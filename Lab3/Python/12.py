def calculate_average(measurements):
    total = 0
    for item in measurements:
        total += item
    return total / len(measurements)

def find_minimum(measurements):
    minimum = measurements[0]
    for item in measurements[1:]:
        if item < minimum:
            minimum = item
    return minimum

def find_maximum(measurements):
    maximum = measurements[0]
    for item in measurements[1:]:
        if item > maximum:
            maximum = item
    return maximum

def count_above_average(measurements):
    avg = calculate_average(measurements)
    count = 0
    for item in measurements:
        if item > avg:
            count += 1
    return count

def find_value(measurements, target):
    for i in range(len(measurements)):
        if measurements[i] == target:
            return i
    return -1

def analyze_measurements(measurements):
    return (
        find_minimum(measurements),
        find_maximum(measurements),
        calculate_average(measurements),
    )

data = [14, 28, 9, 45, 62, 31, 18, 5, 80, 22]

min_val, max_val, avg_val = analyze_measurements(data)

print("Количество измерений:", len(data))
print("Минимальное значение:", min_val)
print("Максимальное значение:", max_val)
print("Среднее значение:", avg_val)
print("Количество значений выше среднего:", count_above_average(data))

target = 45
print(f"Индекс значения {target}:", find_value(data, target))