import csv

def agregar_comp():
    diccionario = {}
    comp = True
    while comp:
        try:
            datos_dic = int(input('Ingrese la cantidad de compras que desea agregar: '))
            comp = False
        except ValueError:
            print('Solo puede ingresar valores enteros.')

    for i in range(datos_dic):
        clave = input('Ingrese el medio de pago de la compra: ')
        valor = None
        bolean = True
        while bolean:
            try:
                valor = int(input('Ingrese la cantidad de compras que realizó: '))
                bolean = False
            except ValueError:
                print('Solo puede ingresar valores enteros.')
        
        if clave in diccionario:
            diccionario[clave] += valor  # Sumar el nuevo valor al existente
        else:
            diccionario[clave] = valor  # Asignar el valor si la clave no existe
        print(diccionario)

    return diccionario

def cargar_datos(nombre_archivo):
    total_compras = {}

    try:
        with open(nombre_archivo, 'r', newline='', encoding='utf-8') as f:
            lector = csv.reader(f)
            # Leer la cabecera
            encabezados = next(lector)
            
            # Determinar los índices de las columnas
            medio_index = encabezados.index('Medio de pago') 
            cantidad_index = encabezados.index('Cantidad de Compras')  
            
            for fila in lector:
                medio = fila[medio_index]
                cantidad = int(fila[cantidad_index])  # Convertir a entero
                
                # Sumar la cantidad al total del medio de pago
                if medio in total_compras:
                    total_compras[medio] += cantidad
                else:
                    total_compras[medio] = cantidad

        return total_compras

    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")
        return None
    except ValueError:
        print("Error al convertir la cantidad a un número entero.")
        return None

def main():
    nombre_archivo = 'pais.csv'

    # Intentar cargar datos existentes
    resultados = cargar_datos(nombre_archivo)

    if resultados is None:
        resultados = {}  # Si no se cargaron datos, inicializar como diccionario vacío

    while True:
        # Preguntar al usuario si desea agregar nuevas compras
        respuesta = input("¿Desea agregar nuevas compras? (s/n): ")
        if respuesta.lower() == 's':
            items = agregar_comp()
            # Abrir el archivo en modo de anexado para agregar nuevas compras
            with open(nombre_archivo, 'a', newline='') as f_append:
                escritor = csv.writer(f_append)
                for clave, valor in items.items():
                    escritor.writerow([clave, valor])
                    # Actualizar el diccionario de resultados
                    if clave in resultados:
                        resultados[clave] += valor
                    else:
                        resultados[clave] = valor
        elif respuesta.lower() == 'n':
            break

        # Consultar el total de compras por medio de pago
        medio_buscado = input("Ingrese el medio de pago para sumar las compras (o 'salir' para terminar): ")
        if medio_buscado.lower() == 'salir':
            break

        # Buscar el total de compras para el medio ingresado
        total = resultados.get(medio_buscado, 0)

        if total > 0:
            print(f"Total de compras con {medio_buscado}: {total}")
        else:
            print(f"No se encontraron compras para el medio de pago: {medio_buscado}")

    print("Operación completada.")


main()