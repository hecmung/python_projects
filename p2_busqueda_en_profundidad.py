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

    while stack:
        nodo_actual = stack.pop()

        if nodo_actual == objetivo:
            return True

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            stack.extend(arbol[nodo_actual])

    return False


def main():
    print("Árbol:")
    imprimir_arbol('A')
    nodo_objetivo = input("\nIngresa el nodo objetivo (por ejemplo, 'F'): ").upper()

    if dfs('A', nodo_objetivo):
        print(f"\nEl nodo {nodo_objetivo} es alcanzable desde el nodo 'A'.")
    else:
        print(f"\nEl nodo {nodo_objetivo} no es alcanzable desde el nodo 'A'.")


main()
