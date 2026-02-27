from Libro import Libro
from Usuario import Usuario

class Biblioteca:
    catalogo = {} # Diccionario para los libros
    usuarios = {} # Diccionario para los usuarios
    prestamos = [] # Tupla para los prestamos
    
    def __init__(self): # Inicialzacion de los atributos en el constructor
        self.catalogo = {}
        self.usuarios = {}
        self.prestamos = []
        
    def registrar_libro(self, isbn, titulo, autor, cantidad_libros): # Registra libros
        if isbn in self.catalogo:
            print("Este libro ya existe en la biblioteca") # Verifico si el libro ya esta en el catalogo para no duplicar la informacion
        else:
            self.catalogo[isbn] = Libro(isbn, titulo, autor, cantidad_libros)
            print("Libro registrado exitosamente")
            
    def buscar_libro_titulo(self, titulo): # Busca libro por titulo
        encontrado = False
        for libro in self.catalogo.values():
            if titulo.lower() in libro.titulo.lower():
                encontrado = True
                print(libro)
        if encontrado == False:
            print("Libro no encontrado")
            
    def buscar_libro_autor(self, autor): # Busca libro por autor
        encontrado = False
        for libro in self.catalogo.values():
            if autor.lower() in libro.autor.lower():
                encontrado = True
                print(libro)
        if encontrado == False:
            print("Libro no encontrado")
    
    def libros_disponibles(self): # Metodo para mostrar la cantidad total de libros en la biblioteca
        cantidad_total = 0        # y la cantidad disponible por cada libro
        print("Libros disponibles: \n")
        for libro in self.catalogo.values():
            print(f"Titulo: {libro.titulo} - cantidad disponible: {libro.ejemplares_disponibles}")
            cantidad_total += libro.ejemplares_disponibles
        print(f"Cantidad total de libros disponibles en la biblioteca {cantidad_total}")
    
    def registrar_usuario(self, id_usuario, nombre): # Registra un usuario
        if id_usuario in self.usuarios:
            print("El usuario ya esta registrado en la biblioteca")
        else:
            self.usuarios[id_usuario] = Usuario(id_usuario, nombre)
            print("Usuario registrado exitosamente")
            
    def mostrar_usuarios(self): # Muestra los datos del usuario
        for usuario in self.usuarios.values():
            print(usuario)
            
    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.catalogo:
            print("El libro no existe.")
            return

        if id_usuario not in self.usuarios:
            print("El usuario no existe.")
            return

        # Máximo 3 préstamos activos
        prestamos_usuario = [prestamo for prestamo in self.prestamos if prestamo[1] == id_usuario]
        if len(prestamos_usuario) >= 3:
            print("El usuario ya no puede realizar prestamos (máximo 3)")
            return

        # Regla: no duplicar préstamo mismo libro mismo usuario
        for prestamo in self.prestamos:
            if prestamo[0] == isbn and prestamo[1] == id_usuario:
                print("El usuario no puede duplicar prestamos")
                return

        libro = self.catalogo[isbn]
        if libro.prestar():
            self.prestamos.append((isbn, id_usuario, ))
            print("Préstamo del libro exitoso")
        else:
            print("No hay libros disponibles para realizar el prestamo")

    def devolver_libro(self, isbn, id_usuario):
        for prestamo in self.prestamos:
            if prestamo[0] == isbn and prestamo[1] == id_usuario:
                self.catalogo[isbn].devolver()
                self.prestamos.remove(prestamo)
                print("Libro devuelto.")
                return
        print("El usuario no ha realizado un prestamo de este libro")

    def top_3_libros(self):
        libros = list(self.catalogo.values())
        libros.sort(key=lambda libro: libro.veces_prestado, reverse=True)

        print("Top 3 libros más prestados:")
        contador = 0
        for libro in libros:
            if contador == 3:
                break
            print(f"{libro.titulo} - {libro.veces_prestado} préstamos")
            contador += 1

    def listar_prestamos_activos(self): # Metodo para listar los prestamos activos que hay en la biblioteca
        print("Préstamos activos:")
        for isbn, id_usuario,  in self.prestamos:
            print(f"Libro: {self.catalogo[isbn].titulo} - Usuario: {self.usuarios[id_usuario].nombre}")