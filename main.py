import json

ruta = "data.json"

def leer():
    try:
        with open(ruta, "r") as file:
            archivo = json.load(file)
            print("File readed")
            return archivo
    except FileNotFoundError:
        print("File not found")

def guardar(data):
    try:
        with open(ruta, "w") as file:
            json.dump(data, file, indent=4)
        print("Datos guardados exitosamente")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")


def crear_ciudad():
    data = leer()
    while True:
        print("Bienvenido al sistema de creacion de ciudades!")
        identificacion = input("Ingrese el id de la ciudad: ")
        nombre = input("Ingrese el nombre de la ciudad: ")
        cp = int(input("Ingresa el codigo postal: "))
        poblacion = int(input("Ingresa el numero de poblacion: "))
        pais = input("Ingresa el nombre del pais: ")
        data["ciudades"][identificacion] = {
            "nombre" : nombre,
            "codigo postal" : cp,
            "poblacion" : poblacion,
            "pais" : pais
        }
        guardar(data)
        print("Ciudad creada exitosamente")
        break
    
def mostrar_ciudades():
    data = leer()
    if "ciudades" in data:
        for id_ciudad, info in data["ciudades"].items():
            print(f"ID: {id_ciudad}")
            print(f"Nombre: {info['nombre']}")
            print(f"Código Postal: {info['codigo postal']}")
            print(f"Población: {info['poblacion']}")
            print(f"País: {info['pais']}")
            print()
    else:
        print("No hay ciudades para mostrar")

def menu():
    while True:
        print("Bienvenidos")
        print("Escoja una opcion : 1. Crear ciudad 2. Editar 3. Buscar ciudad 4. Mostrar ciudades 5. Para Salir")
        opc = int(input(""))

        if opc == 1:
            crear_ciudad()

        elif opc == 2:
            editar_ciudad()

        elif opc ==3:
            buscar_ciudad()

        elif opc ==4:
            mostrar_ciudades()
        
        elif opc == 5:
            print("Saliendo...")
            break

        else: 
            print("Ingrese una opcion valida")

menu()



