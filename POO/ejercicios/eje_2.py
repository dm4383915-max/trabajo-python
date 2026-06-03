class Usuario:
    def __init__(self,documento,nombre,correo,estado,rol):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo 
        self.estado = estado
        self.rol    = rol

    def mostrar_info(self):
        return f"Documento: {self.documento}, Nombre: {self.nombre}, Correo: {self.correo}, Estado: {self.estado}, Rol: {self.rol}"

class SistemaUsuarios:
    def __init__(self):
        self.usuarios=[]

    def registrar_usuario(self):
        documento = int(input("Ingrese el documento del usuario sin puntos: "))

        for us in self.usuarios:
            if us.documento == documento:
                print("Error: El documento ya existe")
                return
        nombre = input("Ingrese el nombre del usuario: ")

        while True:
            correo = input("Ingrese el correo del usuario: ")

            if "@" not in correo or "." not in correo:
                print("Error: El correo no es valido")
            else:
                estado = input("Ingrese el estado del usuario (activo/inactivo): ")

                if estado.lower() not in ["activo", "inactivo"]:
                    print("Error: El estado no es valido")
                else:
                    rol = input("Ingrese el rol del usuario (admin/usuario): ")

                    if rol.lower() not in ["admin", "usuario"]:
                        print("Error: El rol no es valido")
                    else:
                        nuevo_usuario = Usuario(documento, nombre, correo, estado, rol)
                        self.usuarios.append(nuevo_usuario)
                        print("Usuario registrado exitosamente")
                        break



    