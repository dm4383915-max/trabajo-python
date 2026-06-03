class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.__nota = nota

    def get_nota(self):
        return self.__nota
    
    def set_nota(self,nueva_nota):
        if nueva_nota >= 0 and nueva_nota <=5:
            self.__nota = nueva_nota
        else:
            print("Error: Nota invalida")

estudiantes=[]

for i in range(3):
    print(f"Registro estudiante{i+1}")

    nombre = input("Ingrese nombre:")

    while True:
        nota = float(input("Ingrese la nota: "))

        if 0 <= nota <= 5:
            break
        else:
            print("Nota invalida")

    e = Estudiante(nombre,nota)
    estudiantes.append(e)

print("\n --- LISTA DE ESTUDIANTES ---")

for est in estudiantes:
    print("Nombre: ", est.nombre)
    print("Nota: ", est.get_nota(), "\n")

