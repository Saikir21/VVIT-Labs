class Vehicle:

  def __init__(self, brand: str, model: str, year: int):
    self.brand = brand
    self.model = model
    self.year = year
    self._speed = 0

  @property
  def speed(self) -> float:
    return self._speed

  @speed.setter
  def speed(self, value: float) -> None:
    if value < 0:
      raise ValueError("Скорость не может быть отрицательной")
    self._speed = value

  def accelerate(self, value: float) -> None:
    if value > 0:
      self.speed = self.speed + value

  def brake(self, value: float) -> None:
    if value > 0:
      self.speed = max(0.0, self.speed - value)

  def stop(self) -> None:
    self.speed = 0

  def get_info(self) -> str:
    return f"{self.brand} {self.model} ({self.year}), скорость: {self.speed} км/ч"

  def __str__(self) -> str:
    return f"{self.brand} {self.model} ({self.year}), текущая скорость: {self.speed} км/ч"