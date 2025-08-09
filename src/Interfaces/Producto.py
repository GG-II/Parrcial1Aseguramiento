from abc import ABC, abstractmethod

class Producto(ABC):
    @abstractmethod
    def get_nombre(self) -> str:
        pass

    @abstractmethod
    def get_precio(self) -> float:
        pass

    @abstractmethod
    def set_precio(self, precio: float) -> None:
        pass