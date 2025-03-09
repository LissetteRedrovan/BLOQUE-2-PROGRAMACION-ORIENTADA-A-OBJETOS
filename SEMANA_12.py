class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}, Libros Prestados: {len(self.libros_prestados)}"

class Biblioteca:
    def __init__(self):
        self.libros = {}  # ISBN: Libro
        self.usuarios = set()  # IDs de usuario únicos
        self.usuarios_data = {} # id_usuario: Usuario

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' agregado a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"No se encontró ningún libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.usuarios_data[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado con ID {usuario.id_usuario}.")
        else:
            print(f"El ID de usuario {usuario.id_usuario} ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            del self.usuarios_data[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios_data[id_usuario]
            libro = self.libros[isbn]
            if libro not in usuario.libros_prestados:
                usuario.libros_prestados.append(libro)
                print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
            else:
                print(f"El libro '{libro.titulo}' ya está prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios_data[id_usuario]
            libro = self.libros[isbn]
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
            else:
                print(f"El libro '{libro.titulo}' no está prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios_data[id_usuario]
            return usuario.libros_prestados
        else:
            print("Usuario no encontrado.")
            return []

# Ejemplo de uso
biblioteca = Biblioteca()

libro1 = Libro("Habitos Atomicos", "James Clear", "Autoayuda", "978-6077476719")
libro2 = Libro("Dopamina", "Daniel Z. Lieberman y Michael E. Long", "Neurociencia", "978-8411000109")
libro3 = Libro("La magia", "Rhonda Byrne", "Desarrollo personal", "978-9585531178")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

usuario1 = Usuario("Edgar", 1)
usuario2 = Usuario("Lissette", 2)

biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

biblioteca.prestar_libro(1, "978-6077476719")
biblioteca.prestar_libro(2, "978-8411000109")

print("Libros prestados a Edgar:", [libro.titulo for libro in biblioteca.listar_libros_prestados(1)])
print("Libros prestados a Lissette:", [libro.titulo for libro in biblioteca.listar_libros_prestados(2)])

biblioteca.devolver_libro(1, "978-6077476719")

print("Libros prestados a Lissette después de la devolución:", [libro.titulo for libro in biblioteca.listar_libros_prestados(1)])

resultados_busqueda = biblioteca.buscar_libros("autor", "Byrne")
print("Resultados de búsqueda por autor 'Byrne':", [libro.titulo for libro in resultados_busqueda])

biblioteca.dar_baja_usuario(2)