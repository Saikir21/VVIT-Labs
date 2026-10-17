from typing import List
from models.vehicle import Vehicle


class Garage:
    def __init__(self):
        self.vehicles: List[Vehicle] = []

    def add_vehicle(self, vehicle: Vehicle) -> None:
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle: Vehicle) -> None:
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)

    def show_all(self) -> None:
        if not self.vehicles:
            print("Гараж пуст.")
            return
        for vehicle in self.vehicles:
            print(vehicle.get_info())

    def find_by_brand(self, brand: str) -> List[Vehicle]:
        return [v for v in self.vehicles if v.brand.lower() == brand.lower()]