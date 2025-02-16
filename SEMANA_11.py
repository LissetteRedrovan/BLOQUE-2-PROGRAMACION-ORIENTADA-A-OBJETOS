import pickle

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, nombre_archivo):
        with open(nombre_archivo, 'wb') as archivo:
            pickle.dump(self.productos, archivo)

    def cargar_inventario(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'rb') as archivo:
                self.productos = pickle.load(archivo)
        except FileNotFoundError:
            print("Archivo no encontrado. Creando un nuevo inventario.")
            self.productos = {}

def menu():
    inventario = Inventario()
    inventario.cargar_inventario("inventario.pkl")

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id)
        elif opcion == '3':
            id = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(id, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)
        elif opcion == '5':
            inventario.mostrar_inventario()
        elif opcion == '6':
            inventario.guardar_inventario("inventario.pkl")
            print("Inventario guardado.")
        elif opcion == '7':
            inventario.cargar_inventario("inventario.pkl")
            print("Inventario cargado.")
        elif opcion == '8':
            inventario.guardar_inventario("inventario.pkl")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
