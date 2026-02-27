# Esta clase simplemente es donde tengo el menu, instancio un objeto de la clase biblioteca y a partir de la opcion que selecione el usuario mando a llamar el metodo correspondiente
# con lo que el usuario solicito
from Biblioteca import Biblioteca

biblioteca = Biblioteca()

biblioteca.registrar_libro("123", "Juventud en éxtasis", "Carlos Cuauhtémoc Sánchez", 40) # Registro de libro para no tener que hacerlo manualmente cada prueba
biblioteca.registrar_libro("1234", "Crimen y castigo", "Fiódor Dostoyevski", 20)
biblioteca.registrar_libro("12345", "El mundo de Sofía", "Jostein Gaarder", 100)
biblioteca.registrar_libro("456", "Grito desesperado", "Carlos Cuauhtémoc Sánchez", 25)
biblioteca.registrar_libro("980", "Volar sobre el pantano", "Carlos Cuauhtémoc Sánchez", 10)


while True: # El menu de la biblioteca por consola
    print("""
          Bienvenido al menú de la biblioteca
          
          1) Registrar libro
          2) Registrar usuario
          3) Prestar libro
          4) Devolver libro
          5) Buscar libro por titulo
          6) Buscar libro por autor
          7) Listar usuarios
          8) Listrar préstamos activos
          9) Top 3 libros más prestados
          0) Salir
          
          Introduce el número de la acción que desees realizar:""")
    opcion = int(input())
    
    if opcion == 1: # La primera opcion es para registrar el libro, se le piden los datos al usuario
        isbn = input("Teclee el isbn del libro: ")
        titulo = input("Teclee el titulo del libro: ")
        autor = input("Teclee el autor del libro: ")
        ejemplares = int(input("Introduzca la cantidad de libros a registrar: "))
        biblioteca.registrar_libro(isbn, titulo, autor, ejemplares)
        
    elif opcion == 2: # 2da opcion, registra usuarios
        id_usuario = input("Teclee el id del usuario: ")
        nombre = input("Teclee el nombre del usuario: ")
        biblioteca.registrar_usuario(id_usuario, nombre)

    elif opcion == 3: # La tercera opcion, sirve para realizar los prestamos
        isbn = input("Teclee el isbn del libro a prestar: ")
        id_usuario = input("Teclee el nombre del usuario a realizar el prestamo: ")
        biblioteca.prestar_libro(isbn, id_usuario)

    elif opcion == 4: # Devolucion de libro
        isbn = input("Teclee el isbn del libro a devolver: ")
        id_usuario = input("Teclee el nombre del usuario a devolver el libro: ")
        biblioteca.devolver_libro(isbn, id_usuario)

    elif opcion == 5: # Buscar libros por titulo
        titulo = input("Teclee el titulo del libro que quiere buscar: ")
        biblioteca.buscar_por_titulo(titulo)

    elif opcion == 6: # Buscar libros por autor
        autor = input("Teclee el autor del libro que quiere buscar: ")
        biblioteca.buscar_por_autor(autor)

    elif opcion == 7: # Se manda a llamar el metodo de listado de usuarios
        biblioteca.mostrar_usuarios()

    elif opcion == 8: # Se manda a llamar el metodo de listado de prestamos activos
        biblioteca.listar_prestamos_activos()

    elif opcion == 9:
        biblioteca.top_3_libros()

    elif opcion == 0:
        print("Ha salido del sistema de la biblioteca")
        break

    else:
        print("Introduzca una opción válida")