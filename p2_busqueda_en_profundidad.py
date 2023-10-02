arbol = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H', 'I'],
    'F': ['J', 'K'],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}


def imprimir_arbol(nodo, indent=0):
    print('  ' * indent + nodo)
    for hijo in arbol[nodo]:
        imprimir_arbol(hijo, indent + 1)


def dfs(inicio, objetivo):
    visitados = set()
    stack = [inicio]
    camino = []

    while stack:
        nodo_actual = stack.pop()
        camino.append(nodo_actual)

        print(f"Visitando nodo: {nodo_actual}, Stack actual: {stack}")  # Imprimimos el seguimiento

        if nodo_actual == objetivo:
            return True, camino

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            hijos = list(arbol[nodo_actual])
            hijos.reverse()  # invertimos el orden para explorar 'B' antes que 'C'
            for hijo in hijos:
                if hijo not in visitados:
                    stack.append(hijo)

    return False, camino


def main():
    print("Árbol:")
    imprimir_arbol('A')
    nodo_objetivo = input("\nIngresa el nodo objetivo (por ejemplo, 'F'): ").upper()

    es_alcanzable, camino = dfs('A', nodo_objetivo)

    if es_alcanzable:
        print(f"\nEl nodo {nodo_objetivo} es alcanzable desde el nodo 'A'.")
        print(f"Camino: {' -> '.join(camino)}")
    else:
        print(f"\nEl nodo {nodo_objetivo} no es alcanzable desde el nodo 'A'.")
        print(f"Camino intentado: {' -> '.join(camino)}")


main()
