data = [25, 14, 88, 3, 47, 91, 12, 60]

print("Количество:", len(data))
print("Сумма:", sum(data))
print("Минимум:", min(data))
print("Максимум:", max(data))
print("Среднее арифметическое:", sum(data) / len(data))

sorted_copy = sorted(data)
print("Результат sorted():", sorted_copy)

data.sort()
print("Результат data.sort():", data)