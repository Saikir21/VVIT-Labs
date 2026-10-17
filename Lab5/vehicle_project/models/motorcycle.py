from models.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, year: int, has_sidecar: bool):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def move(self) -> str:
        return "Мотоцикл маневрирует в потоке"

    def get_info(self) -> str:
        base_info = super().get_info()
        sidecar_str = "да" if self.has_sidecar else "нет"
        return f"{base_info}, коляска: {sidecar_str}"