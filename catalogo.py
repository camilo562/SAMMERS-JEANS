from dataclasses import dataclass, field
from typing import List, Dict, Optional
import uuid


@dataclass
class Valoracion:
    usuario: str
    estrellas: int
    comentario: str

    def _post_init_(self):
        if not (1 <= self.estrellas <= 5):
            raise ValueError("El número de estrellas debe estar entre 1 y 5.")



@dataclass
class Producto:
    nombre: str
    categoria: str  # Ejemplo: "Jean", "Pantalón", "Jogger"
    precio: float
    descripcion: str
    tallas: List[str]
    colores: List[str]
    stock: int
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    valoraciones: List[Valoracion] = field(default_factory=list)

    def esta_disponible(self) -> bool:
        """Indica si el producto tiene unidades en stock."""
        return self.stock > 0

    def mostrar_detalle(self) -> Dict:
        """Devuelve toda la información del producto en formato de diccionario."""
        return {
            "ID": self.id,
            "Nombre": self.nombre,
            "Categoría": self.categoria,
            "Precio": f"${self.precio:,.2f}",
            "Descripción": self.descripcion,
            "Tallas": self.tallas,
            "Colores": self.colores,
            "Stock": self.stock,
            "Valoraciones": [
                {"Usuario": v.usuario, "Estrellas": v.estrellas, "Comentario": v.comentario}
                for v in self.valoraciones
            ]
        }

    def agregar_valoracion(self, valoracion: Valoracion):
        """Agrega una nueva reseña del usuario."""
        # Evita valoraciones duplicadas por el mismo usuario
        for v in self.valoraciones:
            if v.usuario == valoracion.usuario:
                raise ValueError("El usuario ya ha valorado este producto.")
        self.valoraciones.append(valoracion)

    def promedio_valoraciones(self) -> float:
        """Calcula el promedio de estrellas del producto."""
        if not self.valoraciones:
            return 0
        return round(sum(v.estrellas for v in self.valoraciones) / len(self.valoraciones), 2)


# -----------------------------------------------------
# Clase Catalogo (gestiona todos los productos)
# -----------------------------------------------------
class Catalogo:
    def _init_(self):
        self.productos: List[Producto] = []

    def agregar_producto(self, producto: Producto):
        """Agrega un nuevo producto al catálogo."""
        self.productos.append(producto)

    def listar_por_categoria(self, categoria: str) -> List[Producto]:
        """Devuelve productos filtrados por tipo (ejemplo: Jean, Pantalón, Jogger)."""
        return [p for p in self.productos if p.categoria.lower() == categoria.lower()]

    def filtrar_por_atributo(self, talla: Optional[str] = None, color: Optional[str] = None,
                             precio_min: Optional[float] = None, precio_max: Optional[float] = None) -> List[Producto]:
        """Filtra productos según talla, color o rango de precio."""
        resultado = self.productos

        if talla:
            resultado = [p for p in resultado if talla in p.tallas]
        if color:
            resultado = [p for p in resultado if color.lower() in [c.lower() for c in p.colores]]
        if precio_min is not None and precio_max is not None:
            resultado = [p for p in resultado if precio_min <= p.precio <= precio_max]
        return resultado

    def buscar(self, palabra_clave: str) -> List[Producto]:
        """Busca productos por nombre o categoría."""
        palabra_clave = palabra_clave.lower()
        return [
            p for p in self.productos
            if palabra_clave in p.nombre.lower() or palabra_clave in p.categoria.lower()
        ]

    def obtener_producto_por_id(self, id_producto: str) -> Optional[Producto]:
        """Devuelve un producto por su ID único."""
        for p in self.productos:
            if p.id == id_producto:
                return p
        return None


# -----------------------------------------------------
# Bloque de prueba 
# -----------------------------------------------------
if _name_ == "_main_":
    # Crear catálogo de ejemplo
    catalogo = Catalogo()

    # Crear productos
    jean_azul = Producto(
        nombre="Jean Skinny Azul Mujer",
        categoria="Jean",
        precio=95000,
        descripcion="Jean ajustado para mujer, diseño moderno y elástico.",
        tallas=["S", "M", "L"],
        colores=["Azul", "Negro"],
        stock=10
    )

    pantalon_negro = Producto(
        nombre="Pantalón Formal Negro Hombre",
        categoria="Pantalón",
        precio=120000,
        descripcion="Pantalón clásico para hombre, ideal para oficina o eventos.",
        tallas=["M", "L", "XL"],
        colores=["Negro", "Gris"],
        stock=5
    )

    # Agregar al catálogo
    catalogo.agregar_producto(jean_azul)
    catalogo.agregar_producto(pantalon_negro)

    # Agregar valoraciones
    jean_azul.agregar_valoracion(Valoracion("Laura", 5, "Excelente calidad y comodidad."))
    jean_azul.agregar_valoracion(Valoracion("María", 4, "Buen ajuste, aunque un poco largo."))

    # Ejemplo: Buscar productos
    resultados = catalogo.buscar("Jean")
    print("Resultados de búsqueda para 'Jean':")
    for p in resultados:
        print("-", p.nombre, "-", p.precio)

    # Ejemplo: Filtrar por color
    negros = catalogo.filtrar_por_atributo(color="Negro")
    print("\nProductos color negro:")
    for p in negros:
        print("-", p.nombre)

    # Ejemplo: Mostrar detalles
    print("\nDetalle del producto Jean Azul:")
    detalle = jean_azul.mostrar_detalle()
    for k, v in detalle.items():
        print(f"{k}: {v}")

    
    print("\nPromedio de valoraciones:", jean_azul.promedio_valoraciones())