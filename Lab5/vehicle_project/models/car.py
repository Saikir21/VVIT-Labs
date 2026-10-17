from models.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, brand: str, model: str, year: int, doors: int):
      super().__init__(brand, model, year)
      # Инициализация собственного атрибута
      self.doors = doors

    def get_info(self) -> str:
      base_info = super().get_info()
      return f"{base_info}, дверей: {self.doors}"

    def move(self, distance: float) -> str:
      base_calc = super().move(distance)
      return f"Автомобиль едет по трассе -> {base_calc}"