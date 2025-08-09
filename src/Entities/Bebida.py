from src.Entities.ItemMenu import ItemMenu

class Bebida(ItemMenu):
    def __init__(self, nombre: str, precio: float, volumen_ml: int):
        super().__init__(nombre, precio)
        self._volumen_ml = volumen_ml

    def get_volumen_ml(self) -> int:
        return self._volumen_ml

    def get_descripcion(self) -> str:
        return f"Bebida {self.get_nombre()} de {self._volumen_ml}ml. Precio: ${self.get_precio():.2f}"