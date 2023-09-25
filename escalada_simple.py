def funcion_objetivo(x):
    return -(x - 3) ** 2 + 9


def escalada_simple(x_inicial, paso=0.1, max_iteraciones=100):
    x_actual = x_inicial
    valor_actual = funcion_objetivo(x_actual)

    for _ in range(max_iteraciones):
        # Intentamos aumentar y disminuir x
        x_mayor = x_actual + paso
        x_menor = x_actual - paso

        valor_mayor = funcion_objetivo(x_mayor)
        valor_menor = funcion_objetivo(x_menor)

        if valor_mayor > valor_actual:
            x_actual = x_mayor
            valor_actual = valor_mayor
        elif valor_menor > valor_actual:
            x_actual = x_menor
            valor_actual = valor_menor
        else:
            # Si no hay mejora en ninguna dirección, nos detenemos
            break

    return x_actual


# Ejecutamos la función
x_optimo = escalada_simple(x_inicial=0)
print("El valor óptimo de x es:", x_optimo)
