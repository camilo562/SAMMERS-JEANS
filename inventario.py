# modulo de inventario


#------------clase producto
class Producto:
    def __init__(self, id_producto, nombre, precio, stock, categoria, tallas=None, colores=None ,disponible=True):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria=categoria
        self.tallas = tallas or []
        self.colores = colores or []
        self.disponible = disponible
        self.reseñas=[]



    def verificar_estado(self):
        return "Disponible" if self.disponible else "No disponible"
    


    def reseña(self,usuario,texto,calificacion):
        reseña={
            "usuario":usuario.nombre,
            "texto":texto,
            "calificacion":calificacion
        }
        self.reseñas.append(reseña)



    def mostrar_reseña(self):
        if not self.reseñas:
            print("no hay reseñas disponibles")
            return None
        
        print(f"reseñas para ------{self.nombre}------")
        for i in self.reseñas:
            print(f"Usuario-{i['usuario']} x Reseña-{i['texto']} x Calificacion-{i['calificacion']}")



    def __str__(self):
        return f"Producto({self.id_producto}, {self.nombre}, {self.precio}, stock={self.stock} , Categoria{self.categoria})"


#------------------------------------------------------------------------------------------------------------------------------








# ---------inventario inicial
inventario = {
    1: Producto(1, "jean clasico", 80000, 50, "Caballero",[32, 34, 36], ["azul", "negro"], "Disponible"),
    2: Producto(2, "pantalon cargo", 90000, 30,"Caballero", [34, 36], ["verde", "beige"], "Disponible"),
    3: Producto(3, "pantalon cargo", 90000, 30,"Dama", [34, 36], ["verde", "beige"], "Disponible"),
    4: Producto(4, "jogger deportivo", 70000, 20,"Caballero " ,[30, 32, 34], ["gris", "negro"], "Disponible"),
    5: Producto(5, "jogger deportivo", 70000, 20,"Dama" ,[30, 32, 34], ["gris", "negro"], "Disponible"),
    6: Producto(6, "bermudas", 60000, 15,"caballero", [28, 30, 32], ["azul", "caqui"], "Disponible"),
}




# ---------------clase gestion inventario
class gestion_inventario:
    def __init__(self):
        self.inventario = inventario

    
    # ------buscar producto por nombre solo para reseñas
    def buscar_por_nombre(self, nombre_producto):
        nombre_producto = nombre_producto.lower()
        for producto in self.inventario.values():
            if producto.nombre.lower() == nombre_producto:
                return producto
        return None

    # -------agregar producto
    def agregar_producto(self, producto):
        if producto.id_producto in inventario:
            print("El producto ya existe en el inventario.")
            return False
        
        inventario[producto.id_producto] = producto
        print(f"Producto {producto.nombre} agregado al inventario con éxito.")
        return True
    
    # ---------eliminar producto
    def eliminar_producto(self, producto_id):
        if producto_id not in inventario:
            print("El producto no existe en el inventario.")
            return False
        
        nombre = inventario[producto_id].nombre
        del inventario[producto_id]
        print(f"El producto {nombre} con ID {producto_id} fue eliminado del inventario.")
        return True


    # -----------actualizar stock
    def actualizar_stock(self, producto_id, nueva_cantidad):
        if producto_id not in inventario:
            print("El producto no existe en el inventario.")
            return False
        
        inventario[producto_id].stock = nueva_cantidad
        print(f"Stock de {inventario[producto_id].nombre} actualizado a {nueva_cantidad}.")
        return True



    # -------------mostrar inventario
    def mostrar_inventario(self):
        if not inventario:
            print("El inventario está vacío")
            return
        
        print("\n" + "="*130)
        print(f"{'ID':<5} {'NOMBRE':<25} {'PRECIO':<20} {'STOCK':<15} {'CATEGORIA':<5} {'TALLAS':>15} {'COLORES':>20}")
        print("="*130)
        
        for id_prod, producto in inventario.items():
            if producto.stock > 0:
                print(
                    f"{id_prod:<5} {producto.nombre:<25} ${producto.precio:<15} {producto.stock:>7} {producto.categoria:>20} "
                    f"{str(producto.tallas):>20} {str(producto.colores):>23}"
                )
        
        print("="*130)
        print(f"Total de productos: {len(inventario)}")


inventario_gestion=gestion_inventario()