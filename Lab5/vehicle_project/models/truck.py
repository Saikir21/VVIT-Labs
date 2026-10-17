from models.vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, brand: str, model: str, year: int, max_load: float):
        super().__init__(brand, model, year)
        self.max_load = max_load

    def move(self) -> str:
        return "Грузовик перевозит груз"

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, грузоподъемность: {self.max_load} т"