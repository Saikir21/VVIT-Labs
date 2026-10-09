value = 10

def example():
    value = 20
    local_var = 50
    print("Внутри функции:", value)
    print("Локальная переменная:", local_var)

example()
print("Вне функции:", value)

try:
    print(local_var)
except NameError as error:
    print("Ошибка доступа:", error)