#modulo carrito


class carrito:
    def __init__(self, usuario = None):
        self.usuario = usuario
        self.item = []


    def eliminar_producto(self, producto_id):
        for i in self.item:
            if i['producto'].id == producto_id:
                self.item.remove(i)
                print("Producto eliminado del carrito con exito.")
                return True
        return False
    
        

    def calcular_monto(self):
        pass

    def mostrar_carrito(self):
        if not self.item:
            print("El carrito está vacío.")
            return
        
        for i in self.item:
            print(f"Producto: {i['producto'].nombre}, Cantidad: {i['cantidad']}, Precio Unitario: {i['producto'].precio}")


    def agregar_producto(self, producto,cantidad=1):
        if producto.stok < cantidad:
            print("No hay suficiente stock disponible el stock actual es de:", producto.stok)
            return False

        self.item.append((producto,cantidad))
        print("Producto agregado al carrito con exito.")
        
        for i in self.item:
             if carrito.item['producto'].id == producto.id:
                carrito.item['cantidad'] += cantidad
                print(f" Cantidad actualizada: {producto.nombre} x {carrito.item['cantidad']}")
                return True
    




