from src.Entities.Pizza import Pizza
from src.Entities.Bebida import Bebida
from src.Interfaces.Comida import Comida

def main():
    print("=== Sistema de Pizzería (Demo) ===\n")

    # Crear algunos productos
    pizza = Pizza("Pepperoni", 12.50, ["queso", "pepperoni", "salsa"], False)
    pizza_veg = Pizza("Vegetariana", 11.00, ["queso", "champiñones", "pimientos", "cebolla"], True)
    bebida = Bebida("Coca Cola", 2.00, 500)

    # Mostrar menú
    print("Menú:")
    print("-" * 40)
    for producto in [pizza, pizza_veg, bebida]:
        print(f"- {producto.get_descripcion()}")
        if isinstance(producto, Comida):
            print(f"  Es vegetariana: {'Sí' if producto.es_vegetariana() else 'No'}")
        if isinstance(producto, Bebida):
            print(f"  Volumen: {producto.get_volumen_ml()} ml")
        print("-" * 40)

    # Demostración de cambio de precio
    print("\nActualización de precios:")
    print(f"  Precio Coca Cola (antes): Q{bebida.get_precio():.2f}")
    bebida.set_precio(2.25)
    print(f"  Precio Coca Cola (ahora):  Q{bebida.get_precio():.2f}")

    print(f"\nGracias por usar la demo de la pizzería.")

if __name__ == "__main__":
    main()