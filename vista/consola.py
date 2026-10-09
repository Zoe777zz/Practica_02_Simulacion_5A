"""Capa de vista: parametros en consola."""


def mostrar_parametros(parametros):
    print()
    print("PARAMETROS DE LA SIMULACION")
    print("-" * 40)
    print(f"P0 (poblacion inicial)  : {parametros['p0']}")
    print(f"r (tasa de crecimiento) : {parametros['r']:.4f}")
    print(f"sigma (aleatoriedad)    : {parametros['sigma']}")
    print(f"dt (paso de Euler)      : {parametros['dt']}")
    print(f"tiempo (periodos)       : {parametros['tiempo']}")
    print("-" * 40)
    print()
