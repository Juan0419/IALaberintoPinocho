import heapq

# Definir una clase Nodo para representar cada estado en la matriz
class Nodo:
    def __init__(self, x, y, costo, padre):
        self.x = x
        self.y = y
        self.costo = costo
        self.padre = padre

    # Método que permite comparar nodos para ordenarlos en la cola de prioridad
    def __lt__(self, otro):
        return self.costo < otro.costo

    # Método que devuelve una representación en cadena del nodo
    def __str__(self):
        return f"({self.x}, {self.y}): {self.costo}"
    
    # Función que verifica si una celda está dentro de los límites de la matriz y es transitable

# Función que realiza la búsqueda por costo uniforme
def busqueda_costo_uniforme(matriz, inicio, objetivo):
    # Crear el nodo de inicio y agregarlo a la cola de prioridad
    nodo_inicio = Nodo(inicio[0], inicio[1], 0, None)
    cola_prioridad = [nodo_inicio]
    heapq.heapify(cola_prioridad)
    
    # Crear un diccionario para rastrear los nodos explorados y sus costos
    nodos_explorados = {inicio: 0}
    
    # Ejecutar la búsqueda hasta que la cola de prioridad esté vacía o se encuentre el objetivo
    while len(cola_prioridad) > 0:
        # Extraer el nodo con el costo más bajo de la cola de prioridad
        nodo_actual = heapq.heappop(cola_prioridad)
        
        # Comprobar si se ha alcanzado el objetivo
        if (nodo_actual.x, nodo_actual.y) == objetivo:
            # Reconstruir la ruta desde el nodo objetivo hasta el nodo inicial
            ruta = []
            while nodo_actual is not None:
                ruta.append((nodo_actual.x, nodo_actual.y))
                nodo_actual = nodo_actual.padre
            return list(reversed(ruta))
        
        # Obtener los vecinos del nodo actual y agregarlos a la cola de prioridad si aún no se han explorado
        vecinos = obtener_vecinos(matriz, nodo_actual)
        for vecino in vecinos:
            if es_valido(matriz, vecino.x, vecino.y) and (vecino.x, vecino.y) not in nodos_explorados:
                nodos_explorados[(vecino.x, vecino.y)] = vecino.costo
                heapq.heappush(cola_prioridad, vecino)
    
    # Si no se encuentra el objetivo, devolver None
    return None

# Función que devuelve una lista de los vecinos de un nodo en la matriz
def obtener_vecinos(matriz, nodo):
    vecinos = []
    # Comprobar los vecinos a la izquierda, derecha, arriba y abajo del nodo, evitando los muros
    if nodo.x > 0 and matriz[nodo.x - 1][nodo.y] != 0:
        vecino_izq = Nodo(nodo.x - 1, nodo.y, nodo.costo + matriz[nodo.x - 1][nodo.y], nodo)
        vecinos.append(vecino_izq)
    if nodo.x < len(matriz) - 1 and matriz[nodo.x + 1][nodo.y] != 0:
        vecino_der = Nodo(nodo.x + 1, nodo.y, nodo.costo + matriz[nodo.x + 1][nodo.y], nodo)
        vecinos.append(vecino_der)
    if nodo.y > 0 and matriz[nodo.x][nodo.y - 1] != 0:
        vecino_arr = Nodo(nodo.x, nodo.y - 1, nodo.costo + matriz[nodo.x][nodo.y - 1], nodo)
        vecinos.append(vecino_arr)
    if nodo.y < len(matriz[0]) - 1 and matriz[nodo.x][nodo.y + 1] != 0:
        vecino_abj = Nodo(nodo.x, nodo.y + 1, nodo.costo + matriz[nodo.x][nodo.y + 1], nodo)
        vecinos.append(vecino_abj) 
    
    return vecinos

# Función que verifica si una celda está dentro de los límites de la matriz, es transitable y no es un muro
def es_valido(matriz, x, y):
    filas = len(matriz)
    columnas = len(matriz[0])
    if x < 0 or y < 0 or x >= filas or y >= columnas or matriz[x][y] == -1:
        return False
    return True
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    if x < 0 or y < 0 or x >= filas or y >= columnas or matriz[x][y] == -1:
        return False
    return True
    """