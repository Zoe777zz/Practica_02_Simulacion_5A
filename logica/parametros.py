


def calcular_parametros(datos, sigma, dt, semilla):
    p0 = datos[0]
    tiempo = len(datos) - 1

    # r = promedio del crecimiento relativo de cada periodo
    tasas = []
    for i in range(tiempo):
        tasas.append((datos[i + 1] - datos[i]) / datos[i])
    r = sum(tasas) / len(tasas)

    return {
        "p0": p0,
        "r": r,
        "sigma": sigma,
        "dt": dt,
        "tiempo": tiempo,
        "semilla": semilla,
    }
