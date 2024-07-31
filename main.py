import json

ruta = "data.json"

def leer():
    try:
        with open(ruta, "r") as file:
            archivo = json.load(ruta)
            print("File readed")
            return archivo
    except FileNotFoundError:
        print("File not found")

def cargar():
    try:
        with open(ruta, "w") as file:
            archivo = json.dump(file, ruta, indent=4)
            print("It was readed")
    except FileNotFoundError:
        print("It doesent exist")

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
            mostrar_ciudad()
        
        elif opc == 5:
            print("Saliendo...")
            break

        else: 
            print("Ingrese una opcion valida")

menu()



