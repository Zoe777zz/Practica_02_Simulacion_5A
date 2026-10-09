

import numpy as np


def modelo_estocastico(p0, r, sigma, tiempo, semilla):
    np.random.seed(semilla)

    poblacion = [p0]
    for periodo in range(1, tiempo + 1):
        ruido = np.random.normal(0, sigma)
        actual = poblacion[-1]
        nueva = actual + r * actual + ruido
        # la poblacion no puede ser negativa
        poblacion.append(max(0, nueva))

    vector_tiempo = list(range(tiempo + 1))
    return vector_tiempo, poblacion
