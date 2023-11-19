# Descripción: Este programa es el trabajo final del curso de Estructuras de Datos y Algoritmos 1 de la Universidad EAFIT.

# El objetivo del programa es cargar un archivo JSON con relaciones entre personas y responder las siguientes preguntas:
# - Que persona tiene más amigos y cuantos amigos tiene?
# - Que relación es la más fuerte y cual es su peso?
# - Cuales son las relaciones más fuertes de cada usuario?

# Integrantes:
# - Nicol Franchesca García
# - Thomas Osorio
# - Samuel López
# - Miguel Mercado

# Importar librerías
import json
import networkx as nx
import matplotlib.pyplot as plt

# Nombre de las personas en la lista de relaciones (Nodos)
nombres = ["Juan", "Maria", "Luis", "Ana", "Pedro", "Edison", "Gertrudis", "Rafaella", "Tulio", "Laura", "Carlos",
           "Miguel", "Elena", "Sofia"]

# Función para cargar las relaciones desde un archivo JSON
def cargar_relaciones_desde_json(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo_json:
        relaciones = json.load(archivo_json)
    return relaciones

# Función para construir el grafo dirigido con ponderaciones
def construir_grafo_relaciones(relaciones):
    G = nx.DiGraph()

    for relacion in relaciones:
        id_emisor = relacion["id_emisor"]
        id_receptor = relacion["id_receptor"]
        peso = G.get_edge_data(id_emisor, id_receptor, default={"weight": 0})["weight"] + 1
        G.add_edge(id_emisor, id_receptor, weight=peso)

    return G


# Función para dibujar el grafo dirigido con ponderaciones y nombres en los nodos
def dibujar_grafo(G):
    
    
    pos = nx.circular_layout(G)
    #pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    # Crear diccionario de nombres de nodos
    nombres_nodos = {nodo: f"{nodo}\n({nombres[nodo]})" for nodo in G.nodes()}

    # Dibujar el grafo
    nx.draw(G, pos, with_labels=True, labels=nombres_nodos, node_size=500, node_color='skyblue',
            font_size=10, font_color='black', font_weight='bold', arrowsize=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')
    plt.title("Grafo Dirigido con Ponderaciones")
    plt.show()


# Función para responder las objetivos del reto
def cuales_son_los_mas_amigos(G):
    # Obtener el nodo con mayor grado
    maximo = 0
    for nodo in G.nodes():
        grado = G.degree(nodo)
        if grado > maximo:
            maximo = grado
            nodo_maximo = nodo

    #Aquí se imprime el nodo con mayor grado con su correspondiente nombre
    print(f"La persona con más amigos es {nombres[nodo_maximo]} con {maximo} amigos.")
    return nodo_maximo, maximo

# Función para responder las objetivos del reto
def cual_es_la_relacion_mas_fuerte(G):
    # Obtener la relación más fuerte
    maximo = 0
    for relacion in G.edges():
        peso = G.get_edge_data(relacion[0], relacion[1], default={"weight": 0})["weight"]
        if peso > maximo:
            maximo = peso
            relacion_maxima = relacion

    # Aquí se imprime la relación más fuerte con su correspondiente peso
    print(f"La relación más fuerte es entre {nombres[relacion_maxima[0]]} y {nombres[relacion_maxima[1]]} con un peso de {maximo}.")
    return relacion_maxima, maximo

# Función para responder las objetivos del reto
def listas_mas_fuertes_de_amigos(G):
    # Obtener las relaciones más fuertes de cada nodo
    relaciones_mas_fuertes = []
    for nodo in G.nodes():
        maximo = 0
        for relacion in G.edges(nodo):
            peso = G.get_edge_data(relacion[0], relacion[1], default={"weight": 0})["weight"]
            if peso > maximo:
                maximo = peso
                relacion_maxima = relacion
        relaciones_mas_fuertes.append(relacion_maxima)

    # Aquí se imprime la relación más fuerte de cada nodo con su correspondiente peso
    for relacion in relaciones_mas_fuertes:
        maximo = G.get_edge_data(relacion[0], relacion[1], default={"weight": 0})["weight"]
        print(f"La relación más fuerte de {nombres[relacion[0]]} es con {nombres[relacion[1]]} con un peso de {maximo}.")
    return relaciones_mas_fuertes


if __name__ == '__main__':
    # Cargar relaciones desde el archivo JSON
    relaciones = cargar_relaciones_desde_json("historial_comunicaciones.json")

    # Construir el grafo dirigido con ponderaciones
    G_relaciones = construir_grafo_relaciones(relaciones)

    # Dibujar el grafo dirigido con ponderaciones y nombres en los nodos
    dibujar_grafo(G_relaciones)

    print("Que persona tiene más amigos y cuantos amigos tiene?")
    # Obtener el nodo con mayor grado
    nodo_maximo, maximo = cuales_son_los_mas_amigos(G_relaciones)
    print("")

    print("Que relación es la más fuerte y cual es su peso?")
    # Obtener la relación más fuerte
    relacion_maxima, maximo = cual_es_la_relacion_mas_fuerte(G_relaciones)
    print("")

    print("Las relaciones más fuertes de cada usuario son:")
    # Obtener las relaciones más fuertes de cada nodo
    relaciones_mas_fuertes = listas_mas_fuertes_de_amigos(G_relaciones)

