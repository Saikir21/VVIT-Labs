from models import Car, Motorcycle, Truck, Vehicle, ElectricCar
from garage import Garage
def task2():
    print("Задание 2")
    v1 = Vehicle("Toyota", "Camry", 2020)
    v2 = Vehicle("Lada", "Vesta", 2022)
    print(v1.brand, v1.model, v1.year, v1._speed)
    print(v2.brand, v2.model, v2.year, v2._speed)
    print("Объекты разные:", v1 is v2)

def task3():
    print("Задание 3")
    car = Vehicle("Toyota", "Camry", 2020)
    car.accelerate(60)
    print("После разгона:", car.get_info())
    car.brake(20)
    print("После торможения:", car.get_info())


def task4():
    print("Задание 4")
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

def task5():
    print("Задание 5")
    car = Vehicle("Toyota", "Camry", 2020)
    car.accelerate(45)


    print("Вывод через print(car):", car)

    message = f"Транспортное средство: {car}"
    print(message)

def task6():
    print("Задание 6")

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

def task7():
    print("Задание 7")

    truck = Truck("KamAZ", "5490", 2019, 18.0)
    moto = Motorcycle("Ural", "Gear Up", 2022, True)

    print("Информация о грузовике:")
    print(truck.get_info())

    print("\nИнформация о мотоцикле:")
    print(moto.get_info())

    # Проверка изменения скорости
    truck.accelerate(40)
    moto.accelerate(80)
    print(f"\nСкорость грузовика после разгона: {truck.speed} км/ч")
    print(f"Скорость мотоцикла после разгона: {moto.speed} км/ч")

def task8():
    print("Задание 8")
    print("Попытка создать объект базового абстрактного класса Vehicle:")
    try:
        v = Vehicle("Неизвестно", "Прототип", 2024)
    except TypeError as error:
        print(f"Ошибка успешно перехвачена: {error}")

    # 2. Проверка работы метода move() у классов-наследников
    print("\nПроверка вызова move() у наследников:")
    car = Car("Ford", "Focus", 2018, 5)
    truck = Truck("KamAZ", "5490", 2019, 18.0)
    moto = Motorcycle("Ural", "Gear Up", 2022, True)

    car.speed = 100
    truck.speed = 50
    moto.speed = 80
    print(car.move(100))
    print(truck.move(200))
    print(moto.move(200))

def task9():
  print("Задание 9")

  car = Car("Ford", "Focus", 2018, 5)
  truck = Truck("KamAZ", "5490", 2019, 18.0)
  moto = Motorcycle("Ural", "Gear Up", 2022, True)

  car.speed = 100
  truck.speed = 50
  moto.speed = 80

  vehicles = [car, truck, moto]

  for v in vehicles:
    # Динамический вызов нужной реализации move() и get_info()
    print(f"Информация: {v.get_info()}")
    print(f"Движение:   {v.move(200)}")
    print("-" * 60)

def task10():
    print("Задание 10")

    # 1. Создание гаража
    garage = Garage()

    car1 = Car("Toyota", "Camry", 2020, 4)
    car2 = Car("Ford", "Focus", 2018, 5)
    truck = Truck("KamAZ", "5490", 2019, 18.0)
    moto = Motorcycle("Ural", "Gear Up", 2022, True)

    garage.add_vehicle(car1)
    garage.add_vehicle(car2)
    garage.add_vehicle(truck)
    garage.add_vehicle(moto)

    print("Содержимое гаража:")
    garage.show_all()

    print("\nПоиск по марке 'Ford':")
    found = garage.find_by_brand("Ford")
    for item in found:
        print("Найдено:", item.get_info())

    print("\nУдаление Toyota Camry из гаража...")
    garage.remove_vehicle(car1)

    print("\nИтоговое содержимое гаража:")
    garage.show_all()

def task12():
    print("Задание 12")

    tesla = ElectricCar("Tesla", "Model 3", 2023, 75.0)
    tesla.speed = 120

    # 2. Проверка работы методов нового класса
    print("Информация об объекте нового класса:")
    print(tesla.get_info())

    print("\nПроверка метода move(240):")
    print(tesla.move(240))

    # 3. Добавление в Garage вместе со стандартными классами
    print("\nИнтеграция нового класса в существующий класс Garage:")
    garage = Garage()
    garage.add_vehicle(Car("Ford", "Focus", 2018, 5))
    garage.add_vehicle(Truck("KamAZ", "5490", 2019, 18.0))
    garage.add_vehicle(tesla)

    garage.show_all()

if __name__ == "__main__":
    task12()
