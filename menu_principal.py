# menu_principal

from inventario import gestion_inventario , Producto , inventario_gestion
from carrito import Carrito , item_carrito
from pedidos import Pedido
import usuarios
from pagos import registrar_pago
import panle_administrador
from catalogo import Catalogo

catalogo_uso = Catalogo()
gestor_usuarios = usuarios.GestionUsuarios() 
inventario_gestion2= gestion_inventario()



while True:
    print("=" * 60)
    print("--------------Bienvenido a SAMMER JEANS--------------------")
    print("=" * 60)

    print(
        "---Seleccione un rol: ---\n"
        "1. Administrador \n"
        "2. Cliente \n"
        "3. Salir"
    )

    opcion = int(input("Ingrese el número correspondiente a su rol: "))

 
    # ADMINISTRADOR

    if opcion == 1:

        while True:
            print("Has seleccionado el rol de Administrador.")
            correo = input("Ingrese su correo: ")
            contraseña = input("Ingrese su contraseña: ")

            if gestor_usuarios.iniciar_sesion_admin(correo, contraseña):
                print("Acceso concedido como Administrador.\n\n")
                panel_admin = panle_administrador.PanelAdministrador(gestor_usuarios)
                panel_admin.mostrar_menu()
                break
            else:
                print("Credenciales incorrectas. Intente de nuevo.")


    #  CLIENTE

    elif opcion == 2:

        print("Has seleccionado el rol de Cliente.\n")

        opc = input(
            "Seleccione una opción:\n"
            "1. Registrarse\n"
            "2. Iniciar sesión\n"
            "3. Continuar como invitado\n"
            "4. olvido su contraseña   \n"

        )

        # REGISTRO DE NUEVO USUARIO
        if opc == '1':
            print("Registro de nuevo usuario:")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            contraseña = input("Contraseña: ")

            nuevo_usuario = usuarios.Usuario(id_usuario=None, nombre=nombre, correo=correo, contraseña=contraseña)

            if gestor_usuarios.registrar_usuario(nuevo_usuario):
                print("Registro exitoso! Ahora puedes iniciar sesión para comprar.")
            else:
                print("No se pudo completar el registro.")

            print("Redirigiendo al menú principal...\n")

        # INICIO DE SESION CLIENTE
        elif opc == '2':
            print("Iniciar sesión de cliente:")
            correo = input("Ingrese su correo: ")
            contraseña = input("Ingrese su contraseña: ")

            if gestor_usuarios.iniciar_sesion_usuario(correo, contraseña):
                usuario_actual = gestor_usuarios.usuarios[correo]
                print(f"Acceso concedido como Cliente. Bienvenido {usuario_actual.nombre}.\n")

                # Crear el carrito para el usuario
                carrito_usuario = Carrito()
                nuevo_pedido = None

                # MENU DEL CLIENTE
                while True:

                    print("\n" + "=" * 50)
                    print("===== MENU CLIENTE =====")
                    print("=" * 50)
                    print("1. Ver catalogo de productos")
                    print("2. Buscar producto")
                    print("3. Agregar producto al carrito")
                    print("4. Ver carrito")
                    print("5. Crear pedido desde el carrito")
                    print("6. Pagar pedido pendiente")
                    print("7. Dejar reseña del producto")
                    print("8. Ver mis pedidos")
                    print("9. Actualizar mis datos")
                    print("10. ver reseñas de productos")
                    print("11. Salir")
                    print("=" * 50)

                    opcion_cliente = input("Seleccione una opción -> ")

                    # 1. MOSTRAR CATALOGO
                    if opcion_cliente == '1':
                        catalogo_uso.mostrar_catalogo()

                    # 2. BUSCAR PRODUCTO
                    elif opcion_cliente == '2':
                        nombre = input("Ingresa el nombre del producto a buscar: ")
                        catalogo_uso.buscar_por_nombre(nombre)

                    # 3. AGREGAR PRODUCTO AL CARRITO
                    elif opcion_cliente == '3':
                        try:
                            print("Agregar productos al carrito")
                            producto_id = int(input("Ingresa el ID del producto -> "))
                            cantidad = int(input("Ingresa la cantidad -> "))

                            if producto_id in inventario_gestion2.inventario:
                                producto = inventario_gestion2.inventario[producto_id]
                                carrito_usuario.agregar_producto(producto, cantidad)
                            else:
                                print("El producto con ese ID no existe.")
                        except ValueError:
                            print("Error: Debes ingresar numeros validos.")

                    # 4. VER CARRITO
                    elif opcion_cliente == '4':
                        carrito_usuario.mostrar_carrito()



                    # 5. CREAR PEDIDO
                    elif opcion_cliente == '5':
                        if carrito_usuario.calcular_monto() == 0:
                            print("El carrito esta vacio. No se puede realizar el pedido.")
                            print("Agrega productos primero (opcion 3).")
                        else:
                            carrito_usuario.mostrar_carrito()

                            direccion = input(
                                "Agrega una direccion de envio antes de confirmar el pedido separado por comas ',' por favor \n"
                                "'EJEMPLO = numero de casa=1-75 x Barrio=Atalaya x ciudad=Cúcuta' -> "
                            ).strip()

                            print("\n" + "=" * 60)
                            print("OPCIONES DE PEDIDO")
                            print("=" * 60)
                            print("1. Crear pedido con TODOS los productos del carrito")
                            print("2. Seleccionar productos específicos para el pedido")
                            print("=" * 60)

                            confirmacion = input("\nSelecciona una opción (1 o 2): ").strip()

                            
                            if confirmacion == '1':
                                usuario_actual = gestor_usuarios.usuarios[correo]
                                nuevo_pedido = Pedido(usuario_actual, carrito_usuario, direccion)

                                if nuevo_pedido.registrar_pedido():
                                    print(f"\nPedido #{nuevo_pedido.id_pedido} creado exitosamente.")
                                    print(f"Total: ${nuevo_pedido.monto_total:.2f}")
                                    print(f"Direccion de envio: {direccion}")
                                    print("-----Debes de pagar en la opcion 6 para que se complete tu envio de manera correcta.----\n\n")
                                    print("----------NOTA SI NO PAGAS TU PEDIDO NO SERA CONFIRMADO Y SERA CANCELADO---------")

                                    carrito_usuario.items.clear()
                                    print("El carrito ha sido vaciado.")
                                else:
                                    print("No se pudo registrar el pedido.")

                            
                            elif confirmacion == '2':
                                print("\n" + "=" * 60)
                                print("SELECCIONAR PRODUCTOS PARA EL PEDIDO")
                                print("=" * 60)
                                
                                
                                items_disponibles = list(carrito_usuario.items.items())
                                
                                if not items_disponibles:
                                    print("No hay productos en el carrito.")
                                    continue
                                
                                print("\nProductos en tu carrito:")
                                for i, (id_prod, item) in enumerate(items_disponibles, 1):
                                    print(f"{i}. {item.producto.nombre}")
                                    print(f"   Cantidad: {item.cantidad}")
                                    print(f"   Precio unitario: ${item.producto.precio}")
                                    print(f"   Subtotal: ${item.calcular_total():.2f}")
                                    print("-" * 60)
                                
                                
                                print("\nIngresa los NÚMEROS de los productos que deseas incluir en el pedido")
                                print("(Separados por comas. Ejemplo: 1,3,4)")
                                
                                seleccion = input("\nProductos a incluir: ").strip()
                                
                                if not seleccion:
                                    print("No seleccionaste ningún producto.")
                                    continue
                                
                                try:
                                    indices_seleccionados = [int(x.strip()) for x in seleccion.split(',')]
                                    
                                    # Validar índices
                                    indices_validos = []
                                    for idx in indices_seleccionados:
                                        if 1 <= idx <= len(items_disponibles):
                                            indices_validos.append(idx)
                                        else:
                                            print(f"Índice {idx} no válido (debe estar entre 1 y {len(items_disponibles)})")
                                    
                                    if not indices_validos:
                                        print("No seleccionaste productos válidos.")
                                        continue
                                    
                                    # Solicitar cantidades para cada producto seleccionado
                                    print("\n" + "=" * 60)
                                    print("ESPECIFICAR CANTIDADES")
                                    print("=" * 60)
                                    
                                    productos_pedido = {}
                                    total_pedido = 0
                                    
                                    for idx in indices_validos:
                                        id_prod, item = items_disponibles[idx - 1]
                                        
                                        print(f"\n{item.producto.nombre}")
                                        print(f"Cantidad disponible en carrito: {item.cantidad}")
                                        
                                        while True:
                                            try:
                                                cantidad_pedido = int(input(f"¿Cuántas unidades deseas incluir? (1-{item.cantidad}): "))
                                                
                                                if 1 <= cantidad_pedido <= item.cantidad:
                                                    productos_pedido[id_prod] = {
                                                        'item': item,
                                                        'cantidad': cantidad_pedido
                                                    }
                                                    subtotal = item.producto.precio * cantidad_pedido
                                                    total_pedido += subtotal
                                                    print(f" {cantidad_pedido} x {item.producto.nombre} agregado (${subtotal:.2f})")
                                                    break
                                                else:
                                                    print(f"Cantidad debe estar entre 1 y {item.cantidad}")
                                            except ValueError:
                                                print("Ingresa un número válido.")
                                    
                                    # Mostrar resumen del pedido
                                    print("\n" + "=" * 60)
                                    print("RESUMEN DEL PEDIDO")
                                    print("=" * 60)
                                    
                                    for id_prod, data in productos_pedido.items():
                                        item = data['item']
                                        cantidad = data['cantidad']
                                        subtotal = item.producto.precio * cantidad
                                        print(f"• {item.producto.nombre} x{cantidad} - ${subtotal:.2f}")
                                    
                                    print("-" * 60)
                                    print(f"TOTAL DEL PEDIDO: ${total_pedido:.2f}")
                                    print(f"Dirección de envío: {direccion}")
                                    print("=" * 60)
                                    
                                    confirmar_pedido = input("\n¿Confirmar este pedido? (si/no): ").lower()
                                    
                                    if confirmar_pedido == 'si':
                                        from carrito import Carrito
                                        carrito_temporal = Carrito()
                                        
                                        for id_prod, data in productos_pedido.items():
                                            item = data['item']
                                            cantidad = data['cantidad']
                                            carrito_temporal.items[id_prod] = item_carrito(item.producto, cantidad)
                                        
                                        usuario_actual = gestor_usuarios.usuarios[correo]
                                        nuevo_pedido = Pedido(usuario_actual, carrito_temporal, direccion)
                                        
                                        if nuevo_pedido.registrar_pedido():
                                            print(f"\n✓ Pedido #{nuevo_pedido.id_pedido} creado exitosamente.")
                                            print(f"Total: ${nuevo_pedido.monto_total:.2f}")
                                            print("-----Debes de pagar en la opcion 6 para que se complete tu envio de manera correcta.----\n\n")
                                            print("----------NOTA SI NO PAGAS TU PEDIDO NO SERA CONFIRMADO Y SERA CANCELADO---------")
                                            
                                            for id_prod, data in productos_pedido.items():
                                                cantidad_pedido = data['cantidad']
                                                
                                                if carrito_usuario.items[id_prod].cantidad == cantidad_pedido:
                                                    del carrito_usuario.items[id_prod]
                                                else:
                                                    carrito_usuario.items[id_prod].cantidad -= cantidad_pedido
                                            
                                            print("\n✓ Carrito actualizado.")
                                            
                                            # Mostrar carrito restante
                                            if carrito_usuario.items:
                                                print("\nProductos restantes en el carrito:")
                                                carrito_usuario.mostrar_carrito()
                                            else:
                                                print("El carrito ha sido vaciado completamente.")
                                        else:
                                            print("No se pudo registrar el pedido.")
                                    else:
                                        print("Pedido cancelado.")
                                
                                except ValueError:
                                    print("Error: Formato inválido. Usa números separados por comas.")
                                except Exception as e:
                                    print(f"Error: {e}")





                    # 6. PAGAR PEDIDO
                    elif opcion_cliente == '6':
                        from pedidos import obtener_pedidos_por_usuario

                        pedidos_usuario = obtener_pedidos_por_usuario(correo)
                        pedidos_pendientes = [p for p in pedidos_usuario if p.estado == "Pendiente"]

                        if not pedidos_pendientes:
                            print("No tienes pedidos pendientes de pago.")
                            print("Crea un pedido primero (opcion 5).")
                        else:
                            print("\n" + "=" * 60)
                            print("PEDIDOS PENDIENTES DE PAGO")
                            print("=" * 60)
                            
                            # Mostrar pedidos con más detalle
                            for p in pedidos_pendientes:
                                print(f"\nPedido #{p.id_pedido}")
                                print(f"  Fecha: {p.fecha}")
                                print(f"  Total: ${p.monto_total:.2f}")
                                print(f"  Estado: {p.estado}")
                                print(f"  Direccion: {p.direccion_envio}")
                                print(f"  Productos: {len(p.items)} items")
                                print("-" * 60)
                            
                            print("=" * 60)

                            try:
                                id_ped = int(input("\nID del pedido a pagar: "))
                                pedido_a_pagar = None

                                for p in pedidos_pendientes:
                                    if p.id_pedido == id_ped:
                                        pedido_a_pagar = p
                                        break

                                if pedido_a_pagar:
                                    # Mostrar detalle completo del pedido
                                    print("\n" + "=" * 60)
                                    print(f"DETALLE DEL PEDIDO #{pedido_a_pagar.id_pedido}")
                                    print("=" * 60)
                                    print(f"Fecha: {pedido_a_pagar.fecha}")
                                    print(f"Direccion de envio: {pedido_a_pagar.direccion_envio}")
                                    print("-" * 60)
                                    print("PRODUCTOS:")
                                    
                                    for id_prod, item in pedido_a_pagar.items.items():
                                        subtotal = item.calcular_total()
                                        print(f"  • {item.producto.nombre}")
                                        print(f"    Cantidad: {item.cantidad}")
                                        print(f"    Precio unitario: ${item.producto.precio}")
                                        print(f"    Subtotal: ${subtotal:.2f}")
                                    
                                    print("-" * 60)
                                    print(f"TOTAL DEL PEDIDO: ${pedido_a_pagar.monto_total:.2f}")
                                    print("=" * 60)

                                    try:
                                        monto_ingresado = float(input("\nCuanto deseas pagar? $"))

                                        if monto_ingresado <= 0:
                                            print("Error: El monto debe ser mayor a cero.")

                                        elif monto_ingresado < pedido_a_pagar.monto_total:
                                            faltante = pedido_a_pagar.monto_total - monto_ingresado
                                            print("\n" + "=" * 60)
                                            print("MONTO INSUFICIENTE")
                                            print("=" * 60)
                                            print(f"Monto ingresado: ${monto_ingresado:.2f}")
                                            print(f"Total del pedido: ${pedido_a_pagar.monto_total:.2f}")
                                            print(f"Te faltan: ${faltante:.2f}")
                                            print("=" * 60)
                                            print("\nNo puedes completar el pago. Necesitas el monto completo.")

                                        elif monto_ingresado > pedido_a_pagar.monto_total:
                                            excedente = monto_ingresado - pedido_a_pagar.monto_total
                                            print("\n" + "=" * 60)
                                            print("MONTO EXCEDENTE")
                                            print("=" * 60)
                                            print(f"Monto ingresado: ${monto_ingresado:.2f}")
                                            print(f"Total del pedido: ${pedido_a_pagar.monto_total:.2f}")
                                            print(f"Excedente: ${excedente:.2f}")
                                            print(f"Su cambio sera de: ${excedente:.2f}")
                                            print("El pago se ajustara al monto exacto.")
                                            print("=" * 60)

                                            confirmacion = input("\nDeseas continuar con el pago exacto? (si/no): ").lower()

                                            if confirmacion == 'si':
                                                monto_ingresado = pedido_a_pagar.monto_total
                                                print(f"\nSe ajustara el pago a ${monto_ingresado:.2f}")

                                                print("\nMetodos de pago disponibles:")
                                                metodos = ["nequi", "bancolombia", "daviplata"]
                                                for i, metodo in enumerate(metodos, 1):
                                                    print(f"  {i}. {metodo.upper()}")

                                                metodo = input("\nMetodo de pago: ").strip().lower()

                                                pago_exitoso = registrar_pago(metodo, monto_ingresado, pedido_a_pagar)

                                                if pago_exitoso:
                                                    print("\n" + "=" * 60)
                                                    print("PAGO EXITOSO!")
                                                    print("=" * 60)
                                                    print(f"Pedido #{pedido_a_pagar.id_pedido} pagado completamente")
                                                    print(f"Monto pagado: ${monto_ingresado:.2f}")
                                                    print(f"Metodo: {metodo.upper()}")
                                                    print(f"ID Pago: #{pago_exitoso.id_pago}")
                                                    print(f"Direccion de envio: {pedido_a_pagar.direccion_envio}")
                                                    print("=" * 60)
                                                    print("\nTu pedido sera enviado a la direccion especificada.")
                                                    print("Gracias por tu compra!")
                                                    print("=" * 60)
                                                    pedido_a_pagar.cambiar_estado("Confirmado")
                                                else:
                                                    print("\nEl pago no se pudo procesar.")
                                            else:
                                                print("Pago cancelado.")

                                        else:
                                            print("\nMonto exacto. Procederemos con el pago.")

                                            print("\nMetodos de pago disponibles:")
                                            metodos = ["nequi", "bancolombia", "daviplata"]
                                            for i, metodo in enumerate(metodos, 1):
                                                print(f"  {i}. {metodo.upper()}")

                                            metodo = input("\nMetodo de pago: ").strip().lower()

                                            pago_exitoso = registrar_pago(metodo, monto_ingresado, pedido_a_pagar)

                                            if pago_exitoso:
                                                print("\n" + "=" * 60)
                                                print("PAGO EXITOSO!")
                                                print("=" * 60)
                                                print(f"Pedido #{pedido_a_pagar.id_pedido} pagado completamente")
                                                print(f"Monto pagado: ${monto_ingresado:.2f}")
                                                print(f"Metodo: {metodo.upper()}")
                                                print(f"ID Pago: #{pago_exitoso.id_pago}")
                                                print(f"Direccion de envio: {pedido_a_pagar.direccion}")
                                                print("=" * 60)
                                                print("\nTu pedido sera enviado a la direccion especificada.")
                                                print("Gracias por tu compra!")
                                                print("=" * 60)
                                                pedido_a_pagar.cambiar_estado("Confirmado")
                                            else:
                                                print("\nEl pago no se pudo procesar.")

                                    except ValueError:
                                        print("Error: Debes ingresar un numero valido.")
                                else:
                                    print("Pedido no encontrado.")

                            except ValueError:
                                print("ID invalido. Debe ser un numero.")




                    # 7. DEJAR RESEÑA
                    elif opcion_cliente == '7':
                        nombre_producto = input("Nombre del producto que desea reseñar: ")

                        producto = inventario_gestion2.buscar_por_nombre(nombre_producto)
                        if not producto:
                            print("No se encontró un producto con ese nombre.")
                        else:
                            texto = input("Escribe tu reseña: ")

                            while True:
                                try:
                                    calificacion = int(input("Calificación (1-5): "))
                                    if 1 <= calificacion <= 5:
                                        break
                                    else:
                                        print("Debe ser un número entre 1 y 5.")
                                except ValueError:
                                    print("Debe ser un número válido.")

                            producto.reseña(usuario_actual, texto, calificacion)  
                            print("¡Gracias! Tu reseña ha sido añadida.")




                    # 8. VER MIS PEDIDOS
                    elif opcion_cliente == '8':
                        from pedidos import listar_pedidos_usuario
                        listar_pedidos_usuario(correo)



                    # 9. ACTUALIZAR DATOS
                    elif opcion_cliente == '9':
                        print("Llena los datos que desees actualizar")
                        correo_actual = input("Ingresa tu correo actual para actualizar tus datos -> ")
                        nombre_nuevo = input("Nombre nuevo o presiona Enter si no desea cambiar -> ") or None
                        correo_nuevo = input("Correo nuevo o presiona Enter si no desea cambiar -> ") or None
                        contraseña_nueva = input("Contraseña nueva o presiona Enter si no desea cambiar -> ") or None

                        if gestor_usuarios.actualizar_usuario(correo_actual, nombre_nuevo, correo_nuevo, contraseña_nueva):
                            print("Datos cambiados con éxito.")
                        else:
                            print("No se pudieron actualizar los datos.")

                    # mostrar reseñas 
                    elif opcion_cliente == '10':
                        print("Mostrando las reseñas registradas")
                        producto.mostrar_reseña()



                    # 11. SALIR
                    elif opcion_cliente == '11':
                        print("Cerrando sesion...")
                        break

                    else:
                        print("Opcion no valida. Intenta nuevamente.")

            else:
                print("Correo o contraseña incorrectos.\n")


        # modo invitado 
        elif opc == '3':
            print("Mostrando catálogo de productos como invitado:")
            catalogo_uso.mostrar_catalogo()

            busqueda = input("Desea buscar un producto? (si/no): ").lower()
            if busqueda == 'si':
                nombre = input("Ingresa el nombre del producto a buscar: ")
                catalogo_uso.buscar_por_nombre(nombre)

            registro = input("Desea registrarse como usuario? (si/no): ").lower()
            if registro == 'si':
                print("Registro de nuevo usuario:")
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                contraseña = input("Contraseña: ")

                nuevo_usuario = usuarios.Usuario(id_usuario=None, nombre=nombre, correo=correo, contraseña=contraseña)

                if gestor_usuarios.registrar_usuario(nuevo_usuario):
                    print("Registro exitoso! Ahora puedes iniciar sesión para comprar.")
                else:
                    print("No se pudo completar el registro.")

                print("Redirigiendo al menú principal...\n")
            else:
                print("Gracias por visitar nuestro catálogo.")



       # recuperacion de contraseña 
        elif opc == '4':
            print("recuperación de contraseña\n")


            correo=input("ingresa tu correo para recuperar tu contraseña -> ")
            if gestor_usuarios.recuperar_contraseña(correo):
                print("puedes iniciar sesion exitosamente con tu nuueva contraseña ")
            else:
                print("recuperacion fallida intentalo nuevamente")

        else:
            print("Opción no válida.")



# salir del sistema 
    elif opcion == 3:
        print("Saliendo del sistema. Hasta luego!")
        break

    else:
        print("Opcion invalida. Intente nuevamente.")
    