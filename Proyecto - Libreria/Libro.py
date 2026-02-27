class Libro:
    
    isbn = ""
    titulo = ""
    autor = ""
    ejemplares_totales = 0
    ejemplares_disponibles = 0
    veces_prestado = 0
    
    def __init__(self, isbn, titulo, autor, ejemplares_totales): # Inicializo el constructor de la clase Libro con los atributos indicados.
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ejemplares_totales = ejemplares_totales
        self.ejemplares_disponibles = ejemplares_totales
        self.veces_prestado = 0 # Para validar posteriormente la cantidad de veces que se ha prestado el libro.
        
    def prestar(self): # Revisa si hay libros disponibles, de ser así, se presta el libro y se actualizan los atributos correspondientes. Si no hay libros disponibles, devuelve False.
        if self.ejemplares_disponibles > 0:
            self.ejemplares_disponibles -= 1
            self.veces_prestado += 1
            return True
        else:
            return False
    
    def devolver(self): # Revisa si ya se presto un libro anteriormente y si sí, se devuelve el libro y vuelve a estar disponible.
        if self.ejemplares_disponibles < self.ejemplares_totales:
            self.ejemplares_disponibles += 1
            return True
        else:
            return False
        
    def __str__(self):
        print(f"Titulo: {self.titulo} - Autor: {self.autor} - ISBN: {self.isbn} - Ejemplares disponibles: {self.ejemplares_disponibles} - Veces prestado: {self.veces_prestado}")