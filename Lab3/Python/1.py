def greet(name):
    print(f"Привет, {name}!")

def square(number):
    return number ** 2

def max_of_two(a, b):
    if a >= b:
        return a
    return b

greet("Антон")
greet("Алексей")
print(square(4))
print(square(7))
print(max_of_two(12, 5))
print(max_of_two(-3, 8))