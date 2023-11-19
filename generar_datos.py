import json
import random
from datetime import datetime, timedelta

# Función para generar una relación de forma aleatoria con fecha
def generar_relacion(id_emisor, id_receptor):
    nombres = ["Juan", "Maria", "Luis", "Ana", "Pedro", "Edison", "Gertrudis", "Rafaella", "Tulio", "Laura", "Carlos", "Miguel", "Elena", "Sofia"]
    mensaje = f"Hola {nombres[id_receptor]}, soy {nombres[id_emisor]}. Amigos!!!."

    # Generar fecha aleatoria entre 2021 y julio de 2023 con hora aleatoria
    fecha = datetime(2021, 1, 1) + timedelta(days=random.randint(0, (datetime(2023, 7, 1) - datetime(2021, 1, 1)).days),
                                               hours=random.randint(0, 23),
                                               minutes=random.randint(0, 59),
                                               seconds=random.randint(0, 59))

    relacion = {
        "id_emisor": id_emisor,
        "nombre_emisor": nombres[id_emisor],
        "id_receptor": id_receptor,
        "nombre_receptor": nombres[id_receptor],
        "mensaje": mensaje,
        "fecha": fecha.strftime("%Y-%m-%d %H:%M:%S")  # Formatear la fecha como cadena
    }
    return relacion

# Función principal
def main(cantidad):
    # Número de relaciones que deseas generar
    n = cantidad

    # Lista para almacenar las relaciones
    relaciones = []

    # Generar n relaciones y agregarlas a la lista
    for _ in range(n):
        id_emisor = random.randint(0, 13)
        id_receptor = random.randint(0, 13)
        while (id_emisor == id_receptor):
            id_receptor = random.randint(0, 13)
        relacion = generar_relacion(id_emisor, id_receptor)
        relaciones.append(relacion)

    # Guardar la lista de relaciones en un archivo JSON
    with open("historial_comunicaciones.json", "w") as archivo_json:
        json.dump(relaciones, archivo_json, indent=2)

    print(f"Se han generado y guardado {n} relaciones en el archivo 'relaciones.json'.")

if __name__ == '__main__':
    main(int(input("Cuantos datos desea generar?: ")))
