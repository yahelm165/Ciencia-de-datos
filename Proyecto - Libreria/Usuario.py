class Usuario:
    
    id_usuario = 0
    nombre = ""
    
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        
    def __str__(self):
        print(f"ID: {self.id_usuario} - Nombre: {self.nombre}")