from abc import abstractmethod
from src.Interfaces.Producto import Producto

class Comida(Producto):
    @abstractmethod
    def es_vegetariana(self) -> bool:
        pass