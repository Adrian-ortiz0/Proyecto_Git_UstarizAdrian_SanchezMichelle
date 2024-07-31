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
            "country" : pais
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

def editar_ciudad():
    data = leer()
    if "ciudades" not in data or not data["ciudades"]:
        print("No hay ciudades para editar.")
        return

    identificacion = input("Ingrese el id de la ciudad que desea editar: ")

    if identificacion not in data["ciudades"]:
        print("Ciudad no encontrada.")
        return

    print("Ciudad encontrada.")
    ciudad = data["ciudades"][identificacion]

    print(f"Nombre actual: {ciudad['nombre']}")
    print(f"Código Postal actual: {ciudad['codigo postal']}")
    print(f"Población actual: {ciudad['poblacion']}")
    print(f"País actual: {ciudad['pais']}")

    nuevo_nombre = input("Ingrese el nuevo nombre de la ciudad (deje en blanco para mantener el actual): ")
    nuevo_cp = input("Ingrese el nuevo código postal (deje en blanco para mantener el actual): ")
    nueva_poblacion = input("Ingrese el nuevo número de población (deje en blanco para mantener el actual): ")
    nuevo_pais = input("Ingrese el nuevo nombre del país (deje en blanco para mantener el actual): ")

    if nuevo_nombre:
        ciudad["nombre"] = nuevo_nombre
    if nuevo_cp:
        ciudad["codigo postal"] = int(nuevo_cp)
    if nueva_poblacion:
        ciudad["poblacion"] = int(nueva_poblacion)
    if nuevo_pais:
        ciudad["pais"] = nuevo_pais
        
    guardar(data)
    print("Ciudad actualizada exitosamente")
    
def buscar_ciudad():
    data = leer()
    if "ciudades" not in data or not data["ciudades"]:
        print("No hay ciudades para buscar.")
        return

    print("Bienvenido al sistema de búsqueda!")
    
    while True:
        try:
            elec = int(input("Deseas buscar por: 1. Nombre ciudad | 2. Código postal | 3. País | 4. Mayor poblacion | 5. Menor poblacion | 6. Salir\n"))
            
            if elec == 1:
                nombre_buscar = input("Ingrese el nombre de la ciudad: ").strip()
                encontrado = False
                for id_ciudad, info in data["ciudades"].items():
                    if info["nombre"].lower() == nombre_buscar.lower():
                        print(f"\nCiudad encontrada: {id_ciudad}")
                        print(f"Nombre: {info['nombre']}")
                        print(f"Código Postal: {info['codigo postal']}")
                        print(f"Población: {info['poblacion']}")
                        print(f"País: {info['pais']}\n")
                        encontrado = True
                        break
                if not encontrado:
                    print("Ciudad no encontrada.")
            
            elif elec == 2:
                cp_buscar = int(input("Ingrese el código postal: "))
                encontrado = False
                for id_ciudad, info in data["ciudades"].items():
                    if info["codigo postal"] == cp_buscar:
                        print(f"\nCiudad encontrada: {id_ciudad}")
                        print(f"Nombre: {info['nombre']}")
                        print(f"Código Postal: {info['codigo postal']}")
                        print(f"Población: {info['poblacion']}")
                        print(f"País: {info['pais']}\n")
                        encontrado = True
                        break
                if not encontrado:
                    print("Ciudad no encontrada.")
            
            elif elec == 3:
                pais_buscar = input("Ingrese el nombre del país: ").strip()
                encontrado = False
                for id_ciudad, info in data["ciudades"].items():
                    if info["pais"].lower() == pais_buscar.lower():
                        print(f"\nCiudad encontrada: {id_ciudad}")
                        print(f"Nombre: {info['nombre']}")
                        print(f"Código Postal: {info['codigo postal']}")
                        print(f"Población: {info['poblacion']}")
                        print(f"País: {info['pais']}\n")
                        encontrado = True
                if not encontrado:
                    print("Ciudad no encontrada.")
            elif elec == 4:
                ciudad_max_poblacion = None
                max_poblacion = -1
                for id_ciudad, info in data["ciudades"].items():
                    if info["poblacion"] > max_poblacion:
                        max_poblacion = info["poblacion"]
                        ciudad_max_poblacion = info
                
                if ciudad_max_poblacion:
                    print(f"\nCiudad con la mayor población:")
                    print(f"ID: {id_ciudad}")
                    print(f"Nombre: {ciudad_max_poblacion['nombre']}")
                    print(f"Código Postal: {ciudad_max_poblacion['codigo postal']}")
                    print(f"Población: {ciudad_max_poblacion['poblacion']}")
                    print(f"País: {ciudad_max_poblacion['pais']}\n")
                else:
                    print("No hay ciudades para mostrar.")
            
            elif elec == 5:
                ciudad_min_poblacion = None
                min_poblacion = 9999999999999999999999999
                for id_ciudad, info in data["ciudades"].items():
                    if info["poblacion"] < min_poblacion:
                        min_poblacion = info["poblacion"]
                        ciudad_min_poblacion = info
                
                if ciudad_min_poblacion:
                    print(f"\nCiudad con la menor población:")
                    print(f"ID: {id_ciudad}")
                    print(f"Nombre: {ciudad_min_poblacion['nombre']}")
                    print(f"Código Postal: {ciudad_min_poblacion['codigo postal']}")
                    print(f"Población: {ciudad_min_poblacion['poblacion']}")
                    print(f"País: {ciudad_min_poblacion['pais']}\n")
                else:
                    print("No hay ciudades para mostrar.")
            
            elif elec == 6:
                print("Saliendo...")
                break
            
            else:
                print("Opción inválida. Por favor, ingrese un número entre 1 y 6.")
        
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
    

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



