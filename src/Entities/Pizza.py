from typing import List
from src.Entities.ItemMenu import ItemMenu
from src.Interfaces.Comida import Comida

class Pizza(ItemMenu, Comida):
    def __init__(self, nombre: str, precio: float, ingredientes: List[str], vegetariana: bool):
        super().__init__(nombre, precio)
        self._ingredientes = ingredientes
        self._vegetariana = vegetariana

    def get_ingredientes(self) -> List[str]:
        return self._ingredientes

    def agregar_ingrediente(self, ingrediente: str) -> None:
        self._ingredientes.append(ingrediente)

    def es_vegetariana(self) -> bool:
        return self._vegetariana

    def get_descripcion(self) -> str:
        ingredientes_str = ", ".join(self._ingredientes)
        return f"Pizza {self.get_nombre()} con {ingredientes_str}. Precio: ${self.get_precio():.2f}"