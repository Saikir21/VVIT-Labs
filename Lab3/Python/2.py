def calculate_rectangle(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

def describe_rectangle(width, height, unit="см"):
    print(f"Ширина: {width} {unit}, Высота: {height} {unit}")

w, h = 8, 4
print("Площадь:", calculate_rectangle(w, h))
print("Периметр:", calculate_perimeter(w, h))
describe_rectangle(w, h)
describe_rectangle(w, h, unit="м")