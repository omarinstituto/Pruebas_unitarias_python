import pytest
from cine import Pelicula

def test_compra_exitosa():
    pelicula = Pelicula("Prueba", 10, 8)
    resultado = pelicula.vender_entradas(5)
    print(resultado)
    print("Asientos restantes:", pelicula.asientos_disponibles)

def test_compra_insuficiente():
    pelicula = Pelicula("Prueba", 3, 8)
    resultado = pelicula.vender_entradas(5)
    print(resultado)
    print("Asientos restantes:", pelicula.asientos_disponibles)

def test_compra_cero_entradas():
    pelicula = Pelicula("Prueba", 10, 8)
    resultado = pelicula.vender_entradas(0)
    print(resultado)
    print("Asientos restantes:", pelicula.asientos_disponibles)

def test_compra_todos_los_asientos():
    pelicula = Pelicula("Prueba", 10, 8)
    resultado = pelicula.vender_entradas(10)
    print(resultado)
    print("Asientos restantes:", pelicula.asientos_disponibles)

if __name__ == "__main__":
    test_compra_exitosa()
    test_compra_insuficiente()
    test_compra_cero_entradas()
    test_compra_todos_los_asientos()