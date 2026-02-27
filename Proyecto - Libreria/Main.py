from Biblioteca import Biblioteca

biblioteca = Biblioteca()

while True:
    print("""
          Bienvenido al menú de la biblioteca
          
          1) Registrar libro
          2) Registrar usuario
          3) Prestar libro
          4) Devolver libro
          5) Buscar libro por titulo
          6) Buscar libro por autor
          7) Libro usuarios
          8) Listrar préstamos activos
          9) Top 3 libros más prestados
          0) Salir
          
          Introduce el número de la acción que desees realizar:""")
    opcion = int(input())
    
    if opcion == 1:
        isbn = input("Teclee el isbn del libro: ")
        titulo = input("Teclee el titulo del libro: ")
        autor = input("Teclee el autor del libro: ")
        ejemplares = int(input("Introduzca la cantidad de libros a registrar: "))
        biblioteca.registrar_libro(isbn, titulo, autor, ejemplares)
        
    elif opcion == 2:
        id_usuario = input("Teclee el id del usuario: ")
        nombre = input("Teclee el nombre del usuario: ")
        biblioteca.registrar_usuario(id_usuario, nombre)

    elif opcion == 3:
        isbn = input("Teclee el isbn del libro a prestar: ")
        id_usuario = input("Teclee el nombre del usuario a realizar el prestamo: ")
        biblioteca.prestar_libro(isbn, id_usuario)

    elif opcion == 4:
        isbn = input("Teclee el isbn del libro a devolver: ")
        id_usuario = input("Teclee el nombre del usuario a devolver el libro: ")
        biblioteca.devolver_libro(isbn, id_usuario)

    elif opcion == 5:
        titulo = input("Teclee el titulo del libro que quiere buscar: ")
        biblioteca.buscar_por_titulo(titulo)

    elif opcion == 6:
        autor = input("Teclee el autor del libro que quiere buscar: ")
        biblioteca.buscar_por_autor(autor)

    elif opcion == 7:
        biblioteca.listar_usuarios()

    elif opcion == 8:
        biblioteca.listar_prestamos_activos()

    elif opcion == 9:
        biblioteca.top_3_libros()

    elif opcion == 0:
        print("Ha salido del sistema de la biblioteca")
        break

    else:
        print("Introduzca una opción válida")