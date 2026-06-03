class Producto:
    def __init__(self, codigo, nombre, precio, cantidad, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    def mostrar_info(self):
        return f"Codigo: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}, Categoria: {self.categoria}"


class SistemaInventario:
    def __init__(self):
        self.productos = []

    def menu(self):
        while True:
            print("""
                  ============ MENU ==============
                  1. Registrar productos
                  2. Mostrar productos
                  3. Buscar producto
                  4. Actualizar producto
                  5. Eliminar producto
                  6. Calcular total inventario
                  7. Mostrar productos agotados
                  8. Guardar archivo
                  9. Salir
                  =================================
                  """)

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.registrar_producto()
            elif opcion == "2":
                self.mostrar_productos()
            elif opcion == "3":
                self.buscar_producto()
            elif opcion == "4":
                self.actualizar_producto()
            elif opcion == "5":
                self.eliminar_producto()
            elif opcion == "6":
                self.calcular_total_inventario()
            elif opcion == "7":
                self.mostrar_agotados()
            elif opcion == "8":
                self.guardar_archivo()
            elif opcion == "9":
                print("Saliendo del sistema...")
                break
            else:
                print("Opcion invalida")

    def registrar_producto(self):
        codigo = input("Ingrese el codigo del producto: ")

        for p in self.productos:
            if p.codigo == codigo:
                print("Error: El codigo ya existe")
                return

        nombre = input("Ingrese el nombre del producto: ")

        while True:
            precio = float(input("Ingrese el precio: "))

            if precio < 0:
                print("No se aceptan precios negativos")
            else:
                cantidad = int(input("Ingrese una cantidad: "))

                if cantidad < 0:
                    print("No se aceptan cantidades negativas")
                else:
                    print("""
                  ===== Categorias de los productos =====
                  1. bebidas
                  2. snacks
                  3. enlatados
                  4. abarrotes
                  5. lacteos 
                  6. Salir
                  =================================
                  """)

                    categoria = input("Ingrese la categoria del producto: ")

                    if categoria == "1":
                        categoria = "bebidas"
                    elif categoria == "2":
                        categoria = "snacks"
                    elif categoria == "3":
                        categoria = "enlatados"
                    elif categoria == "4":
                        categoria = "abarrotes"
                    elif categoria == "5":
                        categoria = "lacteos"
                    else:
                        print("Opcion invalida")
                        continue

                    nuevo_producto = Producto(codigo, nombre, precio, cantidad, categoria)
                    self.productos.append(nuevo_producto)
                    print("El producto ha sido creado correctamente")
                    break

    def mostrar_productos(self):
        if len(self.productos) == 0:
            print("No hay productos registrados")
        else:
            print("\nLISTA DE PRODUCTOS")
            for p in self.productos:
                print(p.mostrar_info())

    def buscar_producto(self):
        print("""
    ===== BUSCAR PRODUCTO =====
    1. Buscar por codigo
    2. Buscar por nombre
    ===========================
    """)

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            codigo_buscar = input("Ingrese el codigo del producto: ")

            for p in self.productos:
                if p.codigo == codigo_buscar:
                    print("\nProducto encontrado:")
                    print(p.mostrar_info())
                    return

            print("Producto no encontrado")

        elif opcion == "2":
            nombre_buscar = input("Ingrese el nombre del producto: ")

            for p in self.productos:
                if p.nombre.lower() == nombre_buscar.lower():
                    print("\nProducto encontrado:")
                    print(p.mostrar_info())
                    return

            print("Producto no encontrado")

        else:
            print("Opcion invalida")

    def actualizar_producto(self):
        codigo_buscar = input("Ingrese el codigo del producto a actualizar: ")

        for p in self.productos:
            if p.codigo == codigo_buscar:

                print("""
            ===== ACTUALIZAR =====
            1. Precio
            2. Cantidad
            3. Categoria
            ======================
            """)
                
                opcion = input("Seleccione una opcion: ")

                if opcion == "1":
                    while True:
                        nuevo_precio = float(input("Ingrese el nuevo precio: "))

                        if nuevo_precio < 0:
                            print("No se aceptan precios negativos")
                        else:
                            p.precio = nuevo_precio
                            print("Precio actualizado correctamente")
                            break
                elif opcion == "2":
                    while True:
                        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

                        if nueva_cantidad < 0:
                            print("No se aceptan cantidades negativas")
                        else:
                            p.cantidad = nueva_cantidad
                            print("Cantidad actualizada correctamente")
                            break
                elif opcion == "3":
                    print("""
            ===== Categorias de los productos =====
            1. bebidas
            2. snacks 
            3. enlatados
            4. abarrotes
            5. lacteos
            6. Salir
            =================================
            """)
                    categoria = input("Ingrese la nueva categoria del producto: ")

                    if categoria == "1":
                        p.categoria = "bebidas"
                    elif categoria == "2":
                        p.categoria = "snacks"
                    elif categoria == "3":
                        p.categoria = "enlatados"
                    elif categoria == "4":
                        p.categoria = "abarrotes"
                    elif categoria == "5":
                        p.categoria = "lacteos"
                    else:
                        print("Opcion invalida")
                        return

                    print("Categoria actualizada correctamente")
                else:
                    print("Opcion invalida")
                return
        print("Producto no encontrado")

    def eliminar_producto(self):
        codigo_eliminar = input("Ingrese el codigo del producto a eliminar: ")

        for p in self.productos:
            if p.codigo == codigo_eliminar:
                self.productos.remove(p)
                print("Producto eliminado correctamente")
                return

        print("Producto no encontrado")

    def calcular_total_inventario(self):
        total = 0

        for p in self.productos:
            total += p.precio * p.cantidad

        print(f"El valor total del inventario es: {total:.2f}")

    def mostrar_agotados(self):
        print("\nProductos agotados:")
        for p in self.productos:
            if p.cantidad == 0:
                print(p.mostrar_info())

    def guardar_archivo(self):
        with open("inventario.txt", "w") as archivo:
            for p in self.productos:
                archivo.write(p.mostrar_info() + "\n")
        print("Archivo guardado correctamente")


sistema = SistemaInventario()
sistema.menu()