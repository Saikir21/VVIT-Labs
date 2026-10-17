from models.car import Car
from models.vehicle import Vehicle

def task1():
    print("Задание 2")
    v1 = Vehicle("Toyota", "Camry", 2020)
    v2 = Vehicle("Lada", "Vesta", 2022)
    print(v1.brand, v1.model, v1.year, v1._speed)
    print(v2.brand, v2.model, v2.year, v2._speed)
    print("Объекты разные:", v1 is v2)

def task2():
    print("Задание 3")
    car = Vehicle("Toyota", "Camry", 2020)
    car.accelerate(60)
    print("После разгона:", car.get_info())
    car.brake(20)
    print("После торможения:", car.get_info())
from models.vehicle import Vehicle


def task3():
    print("Задание 3")
    car = Vehicle("Toyota", "Camry", 2020)

    print("Начальная скорость через property:", car.speed)

    car.speed = 80
    print("Скорость после прямой установки через setter:", car.speed)

    car.accelerate(20)
    print("Скорость после разгона на 20:", car.speed)
    car.brake(50)
    print("Скорость после торможения на 50:", car.speed)

    print("\nПопытка установить отрицательную скорость (-25):")
    try:
        car.speed = -25
    except ValueError as error:
        print(f"Исключение успешно перехвачено: {error}")

    print("Итоговая скорость осталась:", car.speed)

def task4():
  print("Задание 4")
  car = Vehicle("Toyota", "Camry", 2020)
  car.accelerate(45)

  # Прямой вывод объекта через print()
  print("Вывод через print(car):", car)

  # Использование в f-строке
  message = f"Транспортное средство: {car}"
  print(message)

def task5():
  print("Задание 5")

  car = Car("Ford", "Focus", 2018, 5)

  print(f"Марка: {car.brand}")
  print(f"Модель: {car.model}")
  print(f"Год: {car.year}")
  print(f"Количество дверей (собственный атрибут Car): {car.doors}")
  print(f"Начальная скорость (унаследована от Vehicle): {car.speed}")

  car.accelerate(70)
  print(f"Скорость после вызова унаследованного accelerate: {car.speed}")
  car.brake(20)
  print(f"Скорость после вызова унаследованного brake: {car.speed}")

  print("\nВызов переопределенного get_info():")
  print(car.get_info())

  print("\nВызов print(car) через унаследованный __str__:")
  print(car)

  print("\nПроверка типов:")
  print("car является экземпляром Car?", isinstance(car, Car))
  print("car является экземпляром Vehicle?", isinstance(car, Vehicle))
  print("Класс Car является подклассом Vehicle?", issubclass(Car, Vehicle))

if __name__ == "__main__":
  task5()
