numeros = [1, 3, 5, 7, 9, 10, 12, 14]
objetivo = 11

def heuristica(n):
    # La heurística es simplemente la diferencia absoluta con el objetivo
    return abs(n - objetivo)

def primero_el_mejor(lista, objetivo):
    lista_ordenada = sorted(lista, key=heuristica)
    # El número con la menor diferencia respecto al objetivo se considera el mejor
    return lista_ordenada[0]

# Ejecutamos la función
numero_cercano = primero_el_mejor(numeros, objetivo)
print(f"El número más cercano a {objetivo} es:", numero_cercano)
