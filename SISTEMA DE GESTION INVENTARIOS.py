# Definir la función para modificar una línea específica
def modificar_linea_archivo(nombre_archivo, numero_linea, nuevo_contenido):
    try:
        # Leer el contenido original del archivo
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.readlines()

        # Modificar la línea especificada
        if 0 < numero_linea <= len(contenido):
            contenido[numero_linea - 1] = nuevo_contenido + "\n"
        else:
            print("Error: Número de línea fuera de rango.")
            return

        # Reescribir el archivo con la línea modificada
        with open(nombre_archivo, 'w') as archivo:
            archivo.writelines(contenido)
        print("Línea modificada exitosamente.")

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    except PermissionError:
        print(f"Error: Permiso denegado para modificar el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error desconocido: {e}")


# Crear y escribir contenido inicial en un archivo
def crear_archivo_inicial(nombre_archivo):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("Línea 1\n")
            archivo.write("Línea 2\n")
            archivo.write("Línea 3\n")
            print(f"Archivo '{nombre_archivo}' creado exitosamente.")
    except PermissionError:
        print(f"Error: Permiso denegado para crear el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error desconocido al crear el archivo: {e}")


# Leer y mostrar el contenido de un archivo
def mostrar_contenido_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            print(f"\nContenido de '{nombre_archivo}':")
            print(archivo.read())
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    except PermissionError:
        print(f"Error: Permiso denegado para leer el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error desconocido al leer el archivo: {e}")


# Ejemplo de uso
nombre_archivo = 'archivo_ejemplo.txt'

# Crear el archivo inicial y escribir en él
crear_archivo_inicial(nombre_archivo)

# Mostrar el contenido original del archivo
mostrar_contenido_archivo(nombre_archivo)

# Modificar una línea específica del archivo
modificar_linea_archivo(nombre_archivo, 2, "Línea 2 modificada")

# Mostrar el contenido modificado del archivo
mostrar_contenido_archivo(nombre_archivo)

# Añadir una nueva línea al archivo
try:
    with open(nombre_archivo, 'a') as archivo:
        archivo.write("Línea 4 añadida\n")
        print("Línea añadida exitosamente.")
except PermissionError:
    print(f"Error: Permiso denegado para añadir al archivo '{nombre_archivo}'.")
except Exception as e:
    print(f"Error desconocido al añadir al archivo: {e}")

# Mostrar el contenido final del archivo
mostrar_contenido_archivo(nombre_archivo)
