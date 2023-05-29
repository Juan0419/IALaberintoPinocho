from queue import Queue

# Clase Nodo para almacenar información sobre cada estado en nuestro grafo
class Nodo:
    def __init__(self, x, y, costo, padre=None):
        self.x = x
        self.y = y
        self.costo = costo
        self.padre = padre

# Función para obtener los vecinos de un nodo en la matriz
def obtener_vecinos(matriz, nodo):
    vecinos = []

    # Comprobar los vecinos a la izquierda, derecha, arriba y abajo del nodo
    if nodo.x > 0 and matriz[nodo.x - 1][nodo.y] > 0:
        vecino_izq = Nodo(nodo.x - 1, nodo.y, nodo.costo + matriz[nodo.x - 1][nodo.y], nodo)
        vecinos.append(vecino_izq)
    if nodo.x < len(matriz) - 1 and matriz[nodo.x + 1][nodo.y] > 0:
        vecino_der = Nodo(nodo.x + 1, nodo.y, nodo.costo + matriz[nodo.x + 1][nodo.y], nodo)
        vecinos.append(vecino_der)
    if nodo.y > 0 and matriz[nodo.x][nodo.y - 1] > 0:
        vecino_arr = Nodo(nodo.x, nodo.y - 1, nodo.costo + matriz[nodo.x][nodo.y - 1], nodo)
        vecinos.append(vecino_arr)
    if nodo.y < len(matriz[0]) - 1 and matriz[nodo.x][nodo.y + 1] > 0:
        vecino_abj = Nodo(nodo.x, nodo.y + 1, nodo.costo + matriz[nodo.x][nodo.y + 1], nodo)
        vecinos.append(vecino_abj)
    
    return vecinos

# Función para buscar el camino más corto utilizando la técnica de búsqueda amplitud
def busqueda_amplitud(matriz, inicio, objetivo):
    # Crear una cola para almacenar los nodos que debemos visitar
    cola = Queue()

    # Agregar el nodo inicial a la cola de nodos por visitar
    cola.put(inicio)

    # Crear un conjunto para almacenar los nodos ya visitados
    visitados = set()

    # Mientras la cola no esté vacía, seguir visitando nodos
    while not cola.empty():
        # Obtener el siguiente nodo de la cola
        nodo_actual = cola.get()
        #objetivo.padre = nodo_actual
        # Si el nodo actual es el objetivo, regresar el camino hasta él
        if nodo_actual.x == objetivo.x and nodo_actual.y == objetivo.y:
            camino = []
            while nodo_actual:
                camino.append((nodo_actual.x, nodo_actual.y))
                nodo_actual = nodo_actual.padre
            return list(reversed(camino))

        # Obtener los vecinos del nodo actual
        vecinos = obtener_vecinos(matriz, nodo_actual)

        # Añadir los vecinos a la cola de nodos por visitar si no han sido visitados ya
        for vecino in vecinos:
            if vecino not in visitados:
                cola.put(vecino)
                visitados.add(vecino)

    # Si no se encontró un camino hasta el objetivo, regresar None
    return None