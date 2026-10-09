


def modelo_discreto(p0, r, tiempo):
    poblacion = [p0]
    for periodo in range(1, tiempo + 1):
        actual = poblacion[-1]
        incremento = r * actual
        poblacion.append(actual + incremento)

    vector_tiempo = list(range(tiempo + 1))
    return vector_tiempo, poblacion
