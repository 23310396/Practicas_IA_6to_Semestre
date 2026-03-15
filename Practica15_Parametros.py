print("4.2 Parámetros en funciones")

print()
print("Función con un parámetro")

def mensaje(numero):
    print("Ingresa un número:", numero)

mensaje(1)
mensaje(5)

print()
print("Variable y parámetro con el mismo nombre")

def mostrar(numero):
    print("Dentro de la función:", numero)

numero = 1234
mostrar(7)
print("Fuera de la función:", numero)

print()
print("Función con dos parámetros")

def mensaje2(que, numero):
    print("Ingresa", que, "número", numero)

mensaje2("teléfono", 11)
mensaje2("precio", 5)

print()
print("Argumentos posicionales")

def mi_funcion(a, b, c):
    print(a, b, c)

mi_funcion(1, 2, 3)

print()
print("Argumentos con palabra clave")

def introduccion(nombre, apellido):
    print("Hola, mi nombre es", nombre, apellido)

introduccion(nombre="Isaac", apellido="Rodríguez")
introduccion(apellido="Herrera", nombre="Ana")

print()
print("Mezcla de argumentos")

def suma(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

suma(1, 2, 3)
suma(3, c=1, b=2)

print()
print("Valores por defecto")

def intro_pred(nombre, apellido="Rodríguez"):
    print("Hola, mi nombre es", nombre, apellido)

intro_pred("Luis")
intro_pred("Sofía", "Herrera")
intro_pred(nombre="Carlos")

print()
print("Dos valores por defecto")

def intro_completo(nombre="Juan", apellido="Rodríguez"):
    print("Hola, mi nombre es", nombre, apellido)

intro_completo()
intro_completo(apellido="Herrera")

print()
print("Prueba de sección")

print()
print("Pregunta 1")
def intro(a="James Bond", b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro()

print()
print("Pregunta 2")
def intro(a="James Bond", b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro(b="Sean Connery")

print()
print("Pregunta 3")
def intro(a, b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro("Susan")

print()
print("Pregunta 4")
print("def add_numbers(a, b=2, c):")
print("Ese código es incorrecto")
print("porque c no puede ir después de un parámetro con valor por defecto")
