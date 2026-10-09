measurements = (12, 34, 56, 78, 90, 23, 45, 67)
print("Индексация и срез:", measurements[0], measurements[-1], measurements[1:4])

try:
    measurements[0] = 100
except TypeError as error:
    print("Ошибка:", error)

first, second = measurements[0], measurements[1]
print("Распаковка:", first, second)

temp_list = list(measurements)
temp_list[2] = 999
measurements = tuple(temp_list)
print("Результирующий кортеж:", measurements)