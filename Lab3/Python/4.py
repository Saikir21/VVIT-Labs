numbers = [15, 24, 7, 42, 18, 93, 5, 61, 33, 10]
print("Элементы (первый, третий, последний):", numbers[0], numbers[2], numbers[-1])

numbers[1] = 99
numbers.append(105)
numbers.remove(7)

print("Итоговый список:", numbers)
print("Количество элементов:", len(numbers))