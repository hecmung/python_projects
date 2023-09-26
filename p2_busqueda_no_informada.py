grafo = {'a': [('p',4), ('j',15), ('b',1)],
         'b': [('a',1), ('d',2), ('e',2), ('c',3)],
         'j': [('a',15)],
         'p': [('a', 4)],
         'd': [('b',2), ('g',3)],
         'e': [('b',2), ('g',4), ('f',5), ('c',2)],
         'c': [('b',3), ('e',2), ('f',5), ('i',20)],
         'g': [('d',3), ('e',4), ('f',10), ('h',1)],
         'f': [('g',10), ('e',5), ('c',5)],
         'i': [('c',20)],
         'h': [('g',1)]
}

# MUESTRA EL GRAFO ANTES DEL RECORRIDO
print("Muestra el grafo antes del recorrido: \n")
for key, lista in grafo.items():
    print(key)
    print(lista)
print()

visitados = []
pila = []

origen = input("Ingresa un nodo: ")
print("\nLista de recorrido en anchura\n")

# Paso 1: SE COLOCA EL VÉRTICE ORIGEN EN UNA PILA
pila.append(origen)

# Paso 2: MIENTRAS LA PILA NO ESTE VACÍA
while pila:
    # Muestra el estado actual de 'visitados' y 'pila'
    print(f"Visitados: {visitados}")
    print(f"Pila: {pila}")
    print("-" * 50)

    # Paso 3: SACAMOS EL PRIMER VÉRTICE, ESTE SERÁ AHORA EL VÉRTICE ACTUAL
    actual = pila.pop(0)

    # Paso 4: SI EL VÉRTICE ACTUAL NO HA SIDO VISITADO
    if actual not in visitados:
        # Paso 5: PROCESAR (IMPRIMIR) EL VÉRTICE ACTUAL
        print("Vertice actual >", actual)
        # Paso 6: COLOCAR VÉRTICE ACTUAL EN LA LISTA DE VISITADOS
        visitados.append(actual)
        # Paso 7: PARA CADA VÉRTICE QUE EL VÉRTICE ACTUAL TIENE COMO DESTINO
        for vecino, _ in grafo[actual]:
            # Y QUE NO HA SIDO VISITADO
            if vecino not in visitados and vecino not in pila:
                # AGREGAR EL VÉRTICE A LA PILA
                pila.append(vecino)
    print()
