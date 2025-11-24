from inventario import inventario


class Catalogo:

    def __init__(self):
        self.productos = inventario   # inventario real

    # mostrar catálogo (solo productos disponibles y con stock)
    def mostrar_catalogo(self):
        print("\n===== CATALOGO DE PRODUCTOS =====")
        for id_prod, producto in self.productos.items():
            if producto.disponible and producto.stock > 0:
                print(f"ID: {id_prod}")
                print(f"Nombre: {producto.nombre}")
                print(f"Precio: ${producto.precio}")
                print(f"Stock: {producto.stock}")
                print(f"categorias: {producto.categoria}")
                print(f"Tallas disponibles: {producto.tallas}")
                print(f"Colores disponibles: {producto.colores}")
                print("---------------------------------")
        print("=================================\n")


    # buscar por nombre
    def buscar_por_nombre(self, nombre):
        resultados = []
        for i in self.productos.values():
            if nombre.lower() in i.nombre.lower():
                resultados.append(i)

        if not resultados:
            print("No se encontraron productos con ese nombre.")
            return []

        print("\nResultados de búsqueda:")
        for prod in resultados:
            print(f"- {prod.nombre} (${prod.precio}) - ID {prod.id_producto}")

        return resultados

    # obtener producto exacto por ID
    def obtener_producto(self, id_producto):
        if id_producto in self.productos:
            return self.productos[id_producto]
        else:
            print("El producto no existe en el catálogo.")
            return None

    # filtrar por rango de precio
    def filtrar_por_precio(self, minimo, maximo):
        resultados = [
            prod for prod in self.productos.values()
            if prod.precio >= minimo and prod.precio <= maximo and prod.stock > 0
        ]

        if not resultados:
            print("No se encontraron productos en ese rango de precio.")
            return []

        print(f"\nProductos entre ${minimo} y ${maximo}:")
        for prod in resultados:
            print(f"- {prod.nombre} (${prod.precio}) - ID {prod.id_producto}")

        return resultados

    # listar solo jeans y pantalones
    def filtrar_prendas_principales(self):
        claves = ["jean", "pantalon", "jogger", "bermuda"]
        resultados = []

        for prod in self.productos.values():
            if any(c in prod.nombre.lower() for c in claves) and prod.stock > 0:
                resultados.append(prod)

        if not resultados:
            print("No se encontraron prendas principales disponibles.")

        print("\nPrendas principales disponibles:")
        for prod in resultados:
            print(f"- {prod.nombre} (${prod.precio}) - ID {prod.id_producto}")

        return resultados

