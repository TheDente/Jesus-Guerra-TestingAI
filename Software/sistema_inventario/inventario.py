class Inventario:
    def __init__(self, nombre_producto, cantidad_inicial):
        self.nombre_producto = nombre_producto
        self.cantidad = cantidad_inicial

    def mostrar_stock(self):
        print(f"📦 {self.nombre_producto}: {self.cantidad} unidades en inventario.")

    def agregar_stock(self, cantidad):
        self.cantidad += cantidad
        print(f"✅ Se agregaron {cantidad} unidades.")

    def reducir_stock(self, cantidad):
        if cantidad > self.cantidad:
            print("❌ No hay suficiente stock.")
        else:
            self.cantidad -= cantidad
            print(f"🗑️ Se retiraron {cantidad} unidades.")


# 🧪 Prueba básica
inventario = Inventario("Mouse inalámbrico", 10)
inventario.mostrar_stock()

inventario.agregar_stock(5)
inventario.mostrar_stock()

inventario.reducir_stock(3)
inventario.mostrar_stock()

inventario.reducir_stock(20)  # prueba con más de lo disponible
inventario.mostrar_stock()