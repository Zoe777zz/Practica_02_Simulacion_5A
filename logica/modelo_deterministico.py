

import numpy as np


def modelo_deterministico(p0, r, tiempo):
    vector_tiempo = np.arange(0, tiempo + 1)

    poblacion = []
    for t in vector_tiempo:
        p = p0 * np.exp(r * t)
        poblacion.append(p)

    return vector_tiempo, poblacion
