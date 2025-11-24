# modulo carrito

# ---- clase del item del carrito ----
class item_carrito:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_total(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad} = ${self.calcular_total():.2f}"


# ---- clase carrito ----
class Carrito:
    def __init__(self, usuario=None):
        self.usuario = usuario
        self.items = {}  # Diccionario de carrito donde la clave es id_producto y el valor es item_carrito

    def agregar_producto(self, producto, cantidad=1): 
        if producto.id_producto in self.items:
            cantidad_actual = self.items[producto.id_producto].cantidad
            nueva_cantidad = cantidad_actual + cantidad
            
            # ------------Valida si hay suficiente stock para la nueva cantidad
            if nueva_cantidad > producto.stock + cantidad_actual:
                stock_disponible = producto.stock + cantidad_actual - cantidad_actual
                print(f"No hay suficiente stock para {producto.nombre}. Stock disponible: {producto.stock}")
                print(f"Ya tienes {cantidad_actual} en el carrito. Solo puedes agregar {producto.stock} más.")
                print(f"Stock disponible total: {stock_disponible}")
                return False
        
            
            # --------------Actualiza cantidad y resta el  stock
            self.items[producto.id_producto].cantidad = nueva_cantidad
            producto.stock -= cantidad
            print(f"Cantidad actualizada: {nueva_cantidad} unidades de {producto.nombre} en el carrito.")
            return True
        
        else:
            # ----------Valida el stock para producto nuevo
            if producto.stock < cantidad:
                print(f"No hay suficiente stock para {producto.nombre}. Stock disponible: {producto.stock} unidades.")
                return False
            
            # --------Agregar nuevo ítem
            self.items[producto.id_producto] = item_carrito(producto, cantidad)
            
            # ------Resta el stock
            producto.stock -= cantidad
            print(f"Se agregó {producto.nombre} x {cantidad} al carrito.")
            return True
        

# ------------Eliminar producto del carrito
    def eliminar_producto(self, id_producto):
        if id_producto in self.items:
            del self.items[id_producto]
            print(f"Producto con ID {id_producto} eliminado del carrito")
        else:
            print("Ese producto no está en el carrito.")


# ---------Calcular monto total del carrito
    def calcular_monto(self):
        total = 0
        for i in self.items.values():
            total += i.calcular_total()
        return total


# ------------Mostrar contenido del carrito

    def mostrar_carrito(self):
        if not self.items:
            print("Tu carrito está vacío.")
            return
        
        print("\nTU CARRITO:")
        print("=" * 50)
        
        for id_prod, name in self.items.items():
            print(f"ID {id_prod}: {name}")

        print("=" * 50)
        print(f"TOTAL: ${self.calcular_monto():.2f}")
        print("=" * 50)