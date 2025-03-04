from biblioteca import Libro, Biblioteca

def test_libro():
    libro = Libro("1984", "George Orwell", 1949)
    print(libro.titulo, libro.autor, libro.anio, "Prestado:", libro.prestado)
    libro.prestado = True
    print(libro)

def test_agregar_libro():
    biblioteca = Biblioteca()
    libro = Libro("El principito", "Antoine de Saint-Exupéry", 1943)
    biblioteca.agregar_libro(libro)
    print("Libros en la biblioteca:", biblioteca.listar_libros())

def test_eliminar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Don Quijote", "Cervantes", 1605)
    biblioteca.agregar_libro(libro)
    biblioteca.eliminar_libro("Don Quijote")
    print("Libros después de eliminar:", biblioteca.listar_libros())

def test_buscar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Moby Dick", "Herman Melville", 1851)
    biblioteca.agregar_libro(libro)
    encontrado = biblioteca.buscar_libro("Moby Dick")
    print("Libro encontrado:", encontrado)

def test_listar_libros():
    biblioteca = Biblioteca()
    biblioteca.agregar_libro(Libro("Libro 1", "Autor 1", 2000))
    biblioteca.agregar_libro(Libro("Libro 2", "Autor 2", 2010))
    print("Lista de libros:", biblioteca.listar_libros())

def test_prestar_libro():
    biblioteca = Biblioteca()
    libro = Libro("El Hobbit", "Tolkien", 1937)
    biblioteca.agregar_libro(libro)
    print(biblioteca.prestar_libro("El Hobbit"))
    print(biblioteca.prestar_libro("El Hobbit"))
    print(biblioteca.prestar_libro("Libro que no existe"))

def test_devolver_libro():
    biblioteca = Biblioteca()
    libro = Libro("Sherlock Holmes", "Arthur Conan Doyle", 1892)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("Sherlock Holmes")
    print(biblioteca.devolver_libro("Sherlock Holmes"))
    print(biblioteca.devolver_libro("Sherlock Holmes"))
    print(biblioteca.devolver_libro("Libro que no existe"))

if __name__ == "__main__":
    test_libro()
    test_agregar_libro()
    test_eliminar_libro()
    test_buscar_libro()
    test_listar_libros()
    test_prestar_libro()
    test_devolver_libro()