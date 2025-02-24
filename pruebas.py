import csv

def obtener_compras_por_pais(nombre_archivo, pais):
    total_compras = 0

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            lector = csv.reader(f)
            encabezados = next(lector)  # Leer la cabecera
            
            # Determinar los índices de las columnas
            pais_index = encabezados.index('Country')  # Cambia 'Country' por el nombre correcto de la columna
            cantidad_index = encabezados.index('Total')  # Cambia 'Total' por el nombre correcto de la columna
            
            for fila in lector:
                if fila[pais_index] == pais:
                    total_compras += float(fila[cantidad_index])  # Asegúrate de convertir a float si es necesario

        return total_compras

    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")
        return None
    except ValueError:
        print("Error al convertir la cantidad a un número.")
        return None

def main():
    nombre_archivo = 'SalesJan2009.csv'
    pais = input("Ingrese el país para obtener las compras: ")
    
    total = obtener_compras_por_pais(nombre_archivo, pais)
    
    if total is not None:
        print(f"Total de compras en {pais}: {total}")

if __name__ == "__main__":
    main()