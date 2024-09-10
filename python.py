# Diccionario que contiene la biblioteca inicial
biblioteca = {
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "disponible": True},
    "1984": {"autor": "George Orwell", "año": 1949, "disponible": True},
    "El principito": {"autor": "Antoine de Saint-Exupéry", "año": 1943, "disponible": False}
}

# Función para agregar un nuevo libro a la biblioteca
def agregar_libro():
    titulo = input("Introduce el título del libro: ")
    autor = input("Introduce el nombre del autor: ")
    año = int(input("Introduce el año de publicación: "))
    biblioteca[titulo] = {"autor": autor, "año": año, "disponible": True}
    print(f'El libro "{titulo}" ha sido agregado a la biblioteca.')

# Función para prestar un libro
def prestar_libro():
    titulo = input("Introduce el título del libro que quieres prestar: ")
    if titulo in biblioteca:
        if biblioteca[titulo]["disponible"]:
            biblioteca[titulo]["disponible"] = False
            print(f'El libro "{titulo}" ha sido prestado.')
        else:
            print(f'El libro "{titulo}" ya está prestado.')
    else:
        print(f'El libro "{titulo}" no está en la biblioteca.')

# Función para devolver un libro
def devolver_libro():
    titulo = input("Introduce el título del libro que quieres devolver: ")
    if titulo in biblioteca:
        if not biblioteca[titulo]["disponible"]:
            biblioteca[titulo]["disponible"] = True
            print(f'El libro "{titulo}" ha sido devuelto.')
        else:
            print(f'El libro "{titulo}" ya está disponible.')
    else:
        print(f'El libro "{titulo}" no está en la biblioteca.')

# Función para mostrar todos los libros
def mostrar_libros():
    if biblioteca:
        for titulo, info in biblioteca.items():
            estado = "Disponible" if info["disponible"] else "No disponible"
            print(f'Título: {titulo}, Autor: {info["autor"]}, Año: {info["año"]}, Estado: {estado}')
    else:
        print("La biblioteca está vacía.")

# Función para mostrar libros por año de publicación
def libros_por_año():
    año = int(input("Introduce el año de publicación: "))
    libros_encontrados = False
    for titulo, info in biblioteca.items():
        if info["año"] == año:
            libros_encontrados = True
            estado = "Disponible" if info["disponible"] else "No disponible"
            print(f'Título: {titulo}, Autor: {info["autor"]}, Estado: {estado}')
    if not libros_encontrados:
        print(f'No se encontraron libros publicados en el año {año}.')

# Menú principal
def menu():
    while True:
        print("\n--- Menú de Biblioteca ---")
        print("1. Agregar un nuevo libro")
        print("2. Prestar un libro")
        print("3. Devolver un libro")
        print("4. Ver todos los libros")
        print("5. Ver libros por año de publicación")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            prestar_libro()
        elif opcion == "3":
            devolver_libro()
        elif opcion == "4":
            mostrar_libros()
        elif opcion == "5":
            libros_por_año()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elige una opción del 1 al 6.")

# Iniciar el menú
menu()
