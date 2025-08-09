from abc import ABC, abstractmethod
from src.Interfaces.Producto import Producto

class ItemMenu(Producto, ABC):
    def __init__(self, nombre: str, precio: float):
        self._nombre = nombre
        self._precio = precio

    def get_nombre(self) -> str:
        return self._nombre

    def get_precio(self) -> float:
        return self._precio

    def set_precio(self, precio: float) -> None:
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = precio

    @abstractmethod
    def get_descripcion(self) -> str:
        pass