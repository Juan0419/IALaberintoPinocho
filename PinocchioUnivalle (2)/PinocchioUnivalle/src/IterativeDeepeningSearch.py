def ids(matriz, inicio, objetivo):
    profundidad = 0
    while True:
        resultado = dls(matriz, inicio, objetivo, profundidad)
        if resultado == objetivo:
            return ruta[::-1] #return resultado
        profundidad += 1

def dls(matriz, nodo, objetivo, profundidad):
    global ruta
    ruta = []
    if profundidad == 0 and nodo == objetivo:
        ruta.append(nodo)
        return nodo #return nodo
    elif profundidad > 0:
        for vecino in obtener_vecinos(matriz, nodo):
            resultado = dls(matriz, vecino, objetivo, profundidad - 1)
            if resultado == objetivo:
                ruta.append(nodo)
                return resultado #return resultado
    return None

def obtener_vecinos(matriz, nodo):
    filas = len(matriz)
    columnas = len(matriz[0])
    vecinos = []
    x, y = nodo
    if x > 0 and matriz[x-1][y] != 0:
        vecinos.append((x-1,y))
    if x < filas - 1 and matriz[x+1][y] != 0:
        vecinos.append((x+1,y))
    if y > 0 and matriz[x][y-1] != 0:
        vecinos.append((x,y-1))
    if y < columnas - 1 and matriz[x][y+1] != 0:
        vecinos.append((x,y+1))
    return vecinos

""" Ejemplo
matriz = [
    [1,3,1,3,1],
    [4,0,1,1,1],
    [1,1,0,0,5],
    [1,1,1,2,1],
    [0,0,1,1,1]]
inicio = (1, 0)
objetivo = (2, 4)
resul = ids(matriz, inicio, objetivo)
#print(resul,':',matriz[resul[0]][resul[1]]) # (2,4):5
# La ruta sale desde la meta hasta el inicial
#print('ruta:',ruta[::-1]) # con [::-1] invertimos el orden de sus elementos
print('ruta:',resul)
"""
