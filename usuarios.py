# Módulo de usuarios

class Usuario:
    def __init__(self, id_usuario, nombre, correo, contraseña, rol="cliente"):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.rol = rol

    def __str__(self):
        return f"Usuario({self.id_usuario}, {self.nombre}, {self.correo})"


class GestionUsuarios:
    def __init__(self):
        self.usuarios = {
            "camilo@gmail.com": Usuario(1, "camilo", "camilo@gmail.com", "CAMILO123"),
            "ricardo@gmail.com": Usuario(2, "ricardo", "ricardo@gmail.com", "RICARDO123")
        }

        self.admins = {
            "administrador@gmail.com": Usuario(100, "admin", "administrador@gmail.com", "ADMIN123", "admin")
        }


    # ----------Registro de usuario
    def registrar_usuario(self, usuario):
        if usuario.correo in self.usuarios:
            print("El usuario ya existe. No se puede registrar.")
            return False
        
        self.usuarios[usuario.correo] = usuario
        print(f"Usuario {usuario.nombre} registrado con éxito.")
        return True

    # -----------Iniciar sesión usuario

    def iniciar_sesion_usuario(self, correo, contraseña):
        if correo not in self.usuarios:
            print("El usuario no existe.")
            return False

        usuario = self.usuarios[correo]

        if usuario.contraseña != contraseña:
            print("Contraseña incorrecta.")
            return False

        print(f"Inicio de sesión exitoso. Bienvenido {usuario.nombre}.")
        return True


    # -----------Actualizar usuario

    def actualizar_usuario(self, correo_actual, nombre=None, nuevo_correo=None, nueva_contraseña=None):
        if correo_actual not in self.usuarios:
            print("El usuario no existe.")
            return False

        usuario = self.usuarios[correo_actual]

        # Cambiar valores
        if nombre:
            usuario.nombre = nombre
        if nueva_contraseña:
            usuario.contraseña = nueva_contraseña

        # Si cambia el correo, mover la clave del diccionario
        if nuevo_correo:
            usuario.correo = nuevo_correo
            self.usuarios[nuevo_correo] = usuario
            del self.usuarios[correo_actual]

        print(f"Usuario {usuario.nombre} actualizo sus datos de {nuevo_correo} y {nueva_contraseña} de manera correcta.")
        return True
   
   
    #recuperacion de contraseña 

    def recuperar_contraseña(self , correo):
        if correo not in self.usuarios:
            print("el usuario no existe. ")
            return False
        
        usuario=self.usuarios[correo]

        print("\n" + "=" * 60)
        print("RECUPERACION DE CONTRASEÑA")
        print("=" * 60)
        print(f"Usuario encontrado: {usuario.nombre}")
        print("=" * 60)

        print("verifica tu identidad " )
        verificar=input("ingresa tu nombre de usuario:").strip()
        if verificar.lower() != usuario.nombre.lower():
            print("acceso denegado")
            return False
        
        nueva_contraseña=input("ingresa la nueva contraeña-> ").strip()
        confirmacion=input("confirma tu contraseña -> ").strip()

        if nueva_contraseña != confirmacion:
            print("la contrasela es distinta a la confirmacion")
            return False
        
        print("su contraseña se cambio con exito.")    
    
        usuario.contraseña = nueva_contraseña
        
        print("\n" + "=" * 60)
        print("CONTRASEÑA RESTABLECIDA EXITOSAMENTE")
        print("=" * 60)
        print("Ahora puedes iniciar sesión con tu nueva contraseña.")
        print("=" * 60)
        
        return True        




    # -------Iniciar sesión admin

    def iniciar_sesion_admin(self, correo, contraseña):
        if correo not in self.admins:
            print("El administrador no existe.")
            return False

        admin = self.admins[correo]

        if admin.contraseña != contraseña:
            print("Contraseña incorrecta.")
            return False

        print(f"Inicio de sesión exitoso. Bienvenido administrador {admin.nombre}.")
        return True

    # -----------Listar usuarios
    def listar_usuarios(self):
        print("\n" + "=" * 70)
        print(f"{'NOMBRE':<20} {'CORREO':<30} {'ROL':<15}")
        print("=" * 70)

        for correo, usuario in self.usuarios.items():
            print(f"{usuario.nombre:<20} {usuario.correo:<30} {usuario.rol:<15}")

        print("=" * 70 + "\n")



