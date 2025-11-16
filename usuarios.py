#modulo de usuarios

class Usuario:
    def __init__(self, id_usuario , nombre, correo ,contraseña, rol="cliente"):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.corrreo = correo
        self.contraseña = contraseña
        self.rol = rol

        def __str__(self):
            return f"Usuario({self.id_usuario}, {self.nombre})"




#sub clase para administrar los usuarios registrados


class GestionUsuarios:
    def __init__(self):
        self.usuarios = []
        self.admins = []


    def registrar_usuario(self):
        for i in self.usuarios:
            if self.id_usuario == Usuario.id_usuario and self.correo == Usuario.correo:
              print("El usuario ya existe no se puede registrar.")
              return False
        self.usuarios.append(Usuario)
        print("Usuario registrado con exito.")




    def iniciar_sesion_usuario(self,nombre, contraseña):
        for i in self.usuarios:
            if i.nombre == nombre and i.contraseña == contraseña:
                print("Inicio de sesión exitoso.")
                return True
        return False




    def actualizar_usuario(self,nombre = None, correo = None, contraseña =None):        
        for i in self.usuarios:
            if nombre:
                i.nombre = nombre
            if correo:
                i.correo = correo
            if contraseña:
                i.contraseña = contraseña
            return True
        
        return False
        
            


    def registar_admin(self):
        for i in self.admins:
            if self.id_usuario == Usuario.id_usuario and self.correo == Usuario.correo:
              print("El administrador ya existe no se puede registrar.")
              return False
        self.admins.append(Usuario)
        print("Administrador registrado con exito.")
        



    def iniciar_sesion_admin(self,nombre, contraseña):
        for i in self.admins:
            if i.nombre == nombre and i.contraseña == contraseña:
                print("Inicio de sesión exitoso.")
                return True
        return False    
    


    def listar_usuarios(self):
        for i in self.usuarios:
            print(i)
