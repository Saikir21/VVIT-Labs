from models.vehicle import Vehicle


class Car(Vehicle):

  def __init__(self, brand: str, model: str, year: int, doors: int):
    # Вызов конструктора родительского класса Vehicle
    super().__init__(brand, model, year)
    # Инициализация собственного атрибута
    self.doors = doors

  def get_info(self) -> str:
    # Получение базовой строки от родителя и дополнение своим атрибутом
    base_info = super().get_info()
    return f"{base_info}, дверей: {self.doors}"