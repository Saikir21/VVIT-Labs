def find_element(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

items = [10, 20, 30, 40, 50, 60]
print("Поиск присутствующего (30):", find_element(items, 30))
print("Поиск отсутствующего (99):", find_element(items, 99))