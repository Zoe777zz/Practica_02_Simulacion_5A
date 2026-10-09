

import numpy as np


def modelo_continuo(p0, r, tiempo, dt):
    pasos = int(round(tiempo / dt))
    vector_tiempo = np.linspace(0, tiempo, pasos + 1)

    poblacion = [p0]
    for paso in range(pasos):
        actual = poblacion[-1]
        cambio = r * actual
        poblacion.append(actual + dt * cambio)

    return vector_tiempo, poblacion
