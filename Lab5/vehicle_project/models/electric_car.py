from models.vehicle import Vehicle


class ElectricCar(Vehicle):

  def __init__(self, brand: str, model: str, year: int, battery: float):
    super().__init__(brand, model, year)
    self.battery = float(battery)

  def move(self, distance: float) -> str:
    # Вызов базового расчета времени из Vehicle.move(distance)
    base_calc = super().move(distance)
    return (
        f"Электромобиль едет на заряде батареи"
        f" ({self.battery} кВт·ч) -> {base_calc}"
    )

  def get_info(self) -> str:
    base_info = super().get_info()
    return f"{base_info}, батарея: {self.battery} кВт·ч"